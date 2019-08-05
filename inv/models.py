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


class UnidadMedida(ModelBase):
    descripcion = models.CharField(max_length=100, help_text='Unidad de medida')

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super().save()

    class Meta:
        verbose_name_plural = 'Unidades de medida'    

class Producto(ModelBase):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barras = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super().save()

    class Meta:
        verbose_name_plural = 'Productos'    
        unique_together = ('codigo', 'codigo_barras')
        