from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', verbose_name="Usuario")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico")
    company = models.CharField(max_length=255, blank=True, verbose_name="Empresa")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('completed', 'Completado'),
        ('on_hold', 'En espera'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects', verbose_name="Cliente")
    name = models.CharField(max_length=255, verbose_name="Nombre del Proyecto")
    description = models.TextField(blank=True, verbose_name="Descripción")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Estado")
    start_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Fin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
    ]
    STATUS_CHOICES = [
        ('todo', 'Pendiente'),
        ('doing', 'En progreso'),
        ('done', 'Hecho'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', verbose_name="Proyecto")
    name = models.CharField(max_length=255, verbose_name="Tarea")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name="Prioridad")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo', verbose_name="Estado")
    due_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Entrega")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.name

class GlobalSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4, default=10.0, verbose_name="Tipo de Cambio Global (1 USD = X Bs)")
    preferred_currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('BOB', 'BOB')], default='USD')

    def __str__(self):
        return f"Configuración de {self.user.username}"

class Invoice(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'Dólares (USD)'),
        ('BOB', 'Bolivianos (Bs)'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagada'),
        ('cancelled', 'Cancelada'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='invoices', verbose_name="Proyecto")
    invoice_number = models.CharField(max_length=50, unique=True, verbose_name="Número de Factura")
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD', verbose_name="Moneda")
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4, default=1.0, verbose_name="Tipo de Cambio")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Estado")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Fecha de Emisión")
    due_date = models.DateField(verbose_name="Fecha de Vencimiento")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"Factura {self.invoice_number} - {self.project.name}"

    @property
    def amount_usd(self):
        if self.currency == 'USD':
            return self.amount
        return self.amount / self.exchange_rate

    @property
    def amount_bob(self):
        if self.currency == 'BOB':
            return self.amount
        return self.amount * self.exchange_rate
