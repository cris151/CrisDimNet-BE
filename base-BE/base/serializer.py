from rest_framework import serializers
from .models import Cliente, Transaction

# Serializer for Cliente model
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'direccion', 'telefono', 'correo', 'estado', 'cedula']

# Serializer for Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'cliente_fk', 'fecha', 'monto', 'tipo_transaccion', 'descripcion']
 