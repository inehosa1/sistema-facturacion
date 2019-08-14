from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin

from django.views import generic
from django.urls import reverse_lazy
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from base.views import SinPrivilegios
# Create your views here.



class CategiaView(SinPrivilegios, generic.ListView):
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = 'inv/categoria_list.html'    

class CategoriaNew(SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.add_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'    
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = 'Categoria creada satisfatoriamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, generic.UpdateView):
    permission_required = 'inv.change_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'    
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = 'Categoria actualizada satisfatoriamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

class CategoriaDel(generic.DeleteView):
    permission_required = 'inv.delete_categoria'
    model = Categoria
    template_name = 'inv/catalogos_del.html'    
    success_url = reverse_lazy('inv:categoria_list')


class SubCategiaView(SinPrivilegios, generic.ListView):
    permission_required = 'inv.view_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'    

class SubCategoriaNew(generic.CreateView):
    permission_required = 'inv.add_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'    
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class SubCategoriaEdit(generic.UpdateView):
    permission_required = 'inv.change_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'    
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

class SubCategoriaDel(generic.DeleteView):
    permission_required = 'inv.delete_subcategoria'
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'    
    success_url = reverse_lazy('inv:subcategoria_list')



class MarcaView(SinPrivilegios, generic.ListView):    
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = 'inv/marca_list.html'    

class MarcaNew(generic.CreateView):
    permission_required = 'inv.add_marca'
    model = Marca
    template_name = 'inv/marca_form.html'    
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class MarcaEdit(generic.UpdateView):
    permission_required = 'inv.change_marca'
    model = Marca
    template_name = 'inv/marca_form.html'    
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.delete_marca', login_url='base:sinprivilegios')
def marca_inactiva(request, id):
    marca = Marca.objects.get(pk=id)
    context = {}
    template_name='inv/catalogos_del.html'

    if not marca:
        return redirect('inv:marca_list')
    
    if request.method == 'GET':
        context = {'obj': marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca inactivada')
        return redirect('inv:marca_list')

    return render(request, template_name, context)

class UnidadMedidaView(generic.ListView):
    permission_required = 'inv.view_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/unidadmedida_list.html'    

class UnidadMedidaNew(generic.CreateView):
    permission_required = 'inv.add_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'    
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inv:unidadmedida_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class UnidadMedidaEdit(generic.UpdateView):
    permission_required = 'inv.change_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'    
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inv:unidadmedida_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.delete_unidadmedida', login_url='base:sinprivilegios')
def unidadmedida_inactiva(request, id):
    unidadmedida = UnidadMedida.objects.get(pk=id)
    context = {}
    template_name='inv/catalogos_del.html'

    if not unidadmedida:
        return redirect('inv:unidadmedida_list')
    
    if request.method == 'GET':
        context = {'obj': marca}

    if request.method == 'POST':
        unidadmedida.estado = False
        unidadmedida.save()
        return redirect('inv:unidadmedida_list')

    return render(request, template_name, context)

class ProductoView(generic.ListView):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = 'inv/producto_list.html'    

class ProductoNew(generic.CreateView):
    permission_required = 'inv.add_producto'
    model = Producto
    template_name = 'inv/producto_form.html'    
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class ProductoEdit(generic.UpdateView):
    permission_required = 'inv.change_producto'
    model = Producto
    template_name = 'inv/producto_form.html'    
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.delete_producto', login_url='base:sinprivilegios')
def producto_inactiva(request, id):
    producto = Producto.objects.get(pk=id)
    context = {}
    template_name='inv/catalogos_del.html'

    if not producto:
        return redirect('inv:producto_list')
    
    if request.method == 'GET':
        context = {'obj': marca}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('inv:producto_list')

    return render(request, template_name, context)