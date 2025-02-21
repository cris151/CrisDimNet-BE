from django.db import models
from django.db.models import Q  # Asegúrate de importar Q

class Cliente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.TextField(blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=50, blank=True, null=True, verbose_name="Teléfono")
    correo = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Correo")
    estado = models.CharField(max_length=50, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], verbose_name="Estado")
    cedula = models.IntegerField(unique=True, verbose_name="Cédula")

    class Meta:
        app_label = 'base' 
        db_table = 'cliente'
        constraints = [
            models.CheckConstraint(check=models.Q(estado__in=['Activo', 'Inactivo']), name='valid_estado'),
            models.UniqueConstraint(fields=['cedula'], name='unique_cedula')
        ]
        indexes = [
            models.Index(fields=['id'], name='cliente_id_index'),
            models.Index(fields=['cedula'], name='cliente_cedula_index')
        ]

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Transaction(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID de Transacción")
    client_fk = models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name="Cliente", related_name='transactions')
    fecha = models.DateField(verbose_name="Fecha")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto")
    tipo_transaccion = models.CharField(max_length=50, choices=[('Pago', 'Pago'), ('Cobro', 'Cobro')], verbose_name="Tipo de Transacción")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        app_label = 'base' 
        db_table = 'transaccion'
        constraints = [
            models.CheckConstraint(check=models.Q(tipo_transaccion__in=['Pago', 'Cobro']), name='valid_tipo_transaccion')
        ]
        indexes = [
            models.Index(fields=['id'], name='transaction_id_index'),
        ]

    def __str__(self):
        return f"Transaction {self.id} for {self.client_fk.nombre} on {self.fecha}"
