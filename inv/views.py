from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

# Create your views here.

class CategiaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'base:login'


class SubCategiaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'base:login'



class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'

class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)


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
        return redirect('inv:marca_list')

    return render(request, template_name, context)

class UnidadMedidaView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'

class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = 'obj'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inv:unidadmedida_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class UnidadMedidaEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = 'obj'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inv:unidadmedida_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)


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

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)


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