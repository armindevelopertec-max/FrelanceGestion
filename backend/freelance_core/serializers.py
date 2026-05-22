from rest_framework import serializers
from .models import Client, Project, Task, Invoice

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.name')
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    amount_usd = serializers.ReadOnlyField()
    amount_bob = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = [
            'id', 'project', 'invoice_number', 'amount', 'currency', 
            'exchange_rate', 'status', 'issue_date', 'due_date', 
            'amount_usd', 'amount_bob'
        ]
