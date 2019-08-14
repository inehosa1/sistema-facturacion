import json

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
 
from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'base:login'

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user        
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id       
        return super().form_valid(form)

def proveedor_inactivar(request, id):
    template_name = 'cmp/inactivar_prv.html'
    context = {}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe {}'.format(id))

    if request.method == 'GET':
        context = {'obj': prv}

    if request.method == 'POST':
        prv.estado = False
        prv.save()
        context = {'obj': 'ok'}
        return HttpResponse('Proveedor inactivado')

    return render(request, template_name, context)