from django.db import models
from django.contrib.auth.models import User


class ModelBase(models.Model):
    '''
    auto_now_add = agrega fecha y hora solo en creacion
    auto_now = cada vez que cambie algo cambia la fecha
    '''
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        ''' No toma encuenta el modelo al crear migraciones'''
        abstract = True