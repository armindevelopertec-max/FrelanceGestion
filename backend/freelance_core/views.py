from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Sum
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from weasyprint import HTML

from .models import Client, Project, Task, Invoice, GlobalSetting
from .serializers import ClientSerializer, ProjectSerializer, TaskSerializer, InvoiceSerializer

# --- Vistas de la API (DRF) ---

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(client__user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(project__client__user=self.request.user)

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(project__client__user=self.request.user)

    @action(detail=True, methods=['get'])
    def download_pdf(self, request, pk=None):
        invoice = self.get_object()
        html_string = render_to_string('freelance_core/invoice_pdf.html', {'invoice': invoice})
        html = HTML(string=html_string)
        pdf = html.write_pdf()
        
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="factura_{invoice.invoice_number}.pdf"'
        return response

# --- Vistas del Dashboard e Interfaz (HTMX) ---

@login_required
@require_http_methods(["GET"])
def invoice_list_view(request):
    invoices = Invoice.objects.filter(project__client__user=request.user).order_by('-issue_date')
    projects = Project.objects.filter(client__user=request.user)
    
    settings, _ = GlobalSetting.objects.get_or_create(user=request.user)
    
    context = {
        'invoices': invoices, 
        'projects': projects,
        'preferred_currency': settings.preferred_currency
    }
    
    return render(request, 'invoices.html', context)

@login_required
@require_http_methods(["POST"])
def update_settings_view(request):
    settings, created = GlobalSetting.objects.get_or_create(user=request.user)
    exchange_rate = request.POST.get('exchange_rate')
    preferred_currency = request.POST.get('preferred_currency')
    
    if exchange_rate:
        settings.exchange_rate = exchange_rate
    if preferred_currency:
        settings.preferred_currency = preferred_currency
    settings.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
@require_http_methods(["POST"])
def invoice_create_view(request):
    project_id = request.POST.get('project_id')
    invoice_number = request.POST.get('invoice_number')
    amount = request.POST.get('amount')
    currency = request.POST.get('currency', 'USD')
    
    # Obtener tipo de cambio global
    settings, _ = GlobalSetting.objects.get_or_create(user=request.user)
    exchange_rate = settings.exchange_rate
    
    due_date = request.POST.get('due_date')
    
    project = Project.objects.get(pk=project_id, client__user=request.user)
    invoice = Invoice.objects.create(
        project=project,
        invoice_number=invoice_number,
        amount=amount,
        currency=currency,
        exchange_rate=exchange_rate,
        due_date=due_date
    )
    return redirect('invoice_list')

@login_required
@require_http_methods(["POST"])
def invoice_update_view(request, pk):
    invoice = Invoice.objects.get(pk=pk, project__client__user=request.user)
    invoice.project_id = request.POST.get('project_id')
    invoice.invoice_number = request.POST.get('invoice_number')
    invoice.amount = request.POST.get('amount')
    invoice.currency = request.POST.get('currency')
    # No actualizamos el exchange_rate en edición para preservar el histórico de esa factura
    # a menos que el usuario explícitamente quiera recalcularla (por simplicidad lo dejamos así)
    invoice.due_date = request.POST.get('due_date')
    invoice.status = request.POST.get('status')
    invoice.save()
    return redirect('invoice_list')

@login_required
@require_http_methods(["POST"])
def invoice_mark_paid_view(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk, project__client__user=request.user)
        invoice.status = 'paid'
        invoice.save()
        return render(request, 'partials/invoice_row.html', {'invoice': invoice})
    except Invoice.DoesNotExist:
        return HttpResponse(status=404)

@method_decorator(login_required, name='dispatch')
class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request):
        user = request.user
        clients_count = Client.objects.filter(user=user).count()
        active_projects = Project.objects.filter(client__user=user, status='active').count()
        
        settings, _ = GlobalSetting.objects.get_or_create(user=user)
        preferred_currency = settings.preferred_currency
        
        # Totales por moneda
        pending_invoices = Invoice.objects.filter(
            project__client__user=user, 
            status='pending'
        )
        
        total_pending = 0
        for inv in pending_invoices:
            if preferred_currency == 'USD':
                total_pending += float(inv.amount_usd)
            else:
                total_pending += float(inv.amount_bob)
        
        data = {
            'clients_count': clients_count,
            'active_projects': active_projects,
            'total_pending': total_pending,
            'preferred_currency': preferred_currency,
            'exchange_rate': settings.exchange_rate,
        }
        
        if request.accepted_renderer.format == 'html':
            return render(request, 'dashboard.html', data)
        return Response(data)

@login_required
@require_http_methods(["GET"])
def client_edit_view(request, pk):
    client = Client.objects.get(pk=pk, user=request.user)
    return render(request, 'client_edit.html', {'client': client})

@login_required
@require_http_methods(["POST"])
def client_update_view(request, pk):
    client = Client.objects.get(pk=pk, user=request.user)
    client.name = request.POST.get('name')
    client.email = request.POST.get('email')
    client.company = request.POST.get('company', '')
    client.save()
    return redirect('client_list')

@login_required
@require_http_methods(["GET"])
def project_edit_view(request, pk):
    project = Project.objects.get(pk=pk, client__user=request.user)
    clients = Client.objects.filter(user=request.user)
    return render(request, 'project_edit.html', {'project': project, 'clients': clients})

@login_required
@require_http_methods(["POST"])
def project_update_view(request, pk):
    project = Project.objects.get(pk=pk, client__user=request.user)
    project.client_id = request.POST.get('client_id')
    project.name = request.POST.get('name')
    project.description = request.POST.get('description', '')
    project.status = request.POST.get('status')
    project.save()
    return redirect('project_list')

@login_required
@require_http_methods(["GET"])
def invoice_edit_view(request, pk):
    invoice = Invoice.objects.get(pk=pk, project__client__user=request.user)
    projects = Project.objects.filter(client__user=request.user)
    return render(request, 'invoice_edit.html', {'invoice': invoice, 'projects': projects})

@login_required
@require_http_methods(["GET"])
def client_list_view(request):
    clients = Client.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'clients.html', {'clients': clients})

@login_required
@require_http_methods(["POST"])
def client_create_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    company = request.POST.get('company', '')
    
    client = Client.objects.create(
        user=request.user,
        name=name,
        email=email,
        company=company
    )
    return render(request, 'partials/client_row.html', {'client': client})

@login_required
@require_http_methods(["DELETE"])
def client_delete_view(request, pk):
    try:
        client = Client.objects.get(pk=pk, user=request.user)
        client.delete()
    except Client.DoesNotExist:
        pass
    return HttpResponse("")

@login_required
@require_http_methods(["GET"])
def project_list_view(request):
    projects = Project.objects.filter(client__user=request.user).order_by('-created_at')
    clients = Client.objects.filter(user=request.user)
    return render(request, 'projects.html', {'projects': projects, 'clients': clients})

@login_required
@require_http_methods(["POST"])
def project_create_view(request):
    client_id = request.POST.get('client_id')
    name = request.POST.get('name')
    description = request.POST.get('description', '')
    
    client = Client.objects.get(pk=client_id, user=request.user)
    project = Project.objects.create(
        client=client,
        name=name,
        description=description
    )
    return render(request, 'partials/project_row.html', {'project': project})

@login_required
@require_http_methods(["DELETE"])
def project_delete_view(request, pk):
    try:
        project = Project.objects.get(pk=pk, client__user=request.user)
        project.delete()
    except Project.DoesNotExist:
        pass
    return HttpResponse("")
