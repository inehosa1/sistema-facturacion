from django.db import models
from base.models import ModelBase

# Create your models here.
class Proveedor(ModelBase):
    descripcion = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    correo = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super().save()

    class Meta:
        verbose_name_plural = 'Proveedores'  