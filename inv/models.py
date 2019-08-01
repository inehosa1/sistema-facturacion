from django.db import models


from base.models import ModelBase

class Categoria(ModelBase):
    descripcion = models.CharField(max_length=100, help_text='Descripción de la categoria', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super().save()

    class Meta:
        verbose_name_plural = 'Categorias'


class SubCategoria(ModelBase):
    categoria =  models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, help_text='Descripción de la categoria')

    def __str__(self):
        return '{}: {}'.format(self.categoria.description, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super().save()

    class Meta:
        verbose_name_plural = 'Sub Categorias'
        unique_together = ('categoria', 'descripcion')

class Marca(ModelBase):
    descripcion = models.CharField(max_length=100, help_text='Descripción de la marca')

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super().save()

    class Meta:
        verbose_name_plural = 'Marca'        
