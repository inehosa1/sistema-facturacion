from django import forms

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto


class FormBase(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })        

class CategoriaForm(FormBase):

    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion':'Descripción de la categoria',
            'estado':"Estado"
        }
        widget = {
            'descripcion': forms.TextInput()
        }

class SubCategoriaForm(FormBase):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {
            'descripcion':'Sub Categoria',
            'estado':"Estado"
        }
        widget = {
            'descripcion': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Seleccione categoría'

class MarcaForm(FormBase):
    
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion':'Marca',
            'estado':"Estado"
        }
        widget = {
            'descripcion': forms.TextInput()
        }
        
class UnidadMedidaForm(FormBase):
    
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado']
        labels = {
            'descripcion':'Unidad de medida',
            'estado':"Estado"
        }
        widget = {
            'descripcion': forms.TextInput()
        }
    
class ProductoForm(FormBase):
    
    class Meta:
        model = Producto
        fields = [
            'codigo','codigo_barras','descripcion', 'estado', 'precio',
            'existencia', 'ultima_compra', 'marca', 'subcategoria',
            'unidad_medida'
        ]
        exclude = [
            'um', 'fm', 'uc', 'fc'
        ]
        widget = {
            'descripcion': forms.TextInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True