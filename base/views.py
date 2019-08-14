from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.views import generic
# Create your views here.

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    raise_exception=False
    redirect_field_name='redirect_to'
    login_url = 'base:login'
    context_object_name = 'obj'

    def handle_no_permission(self):
        if  not self.request.user== AnonymousUser():
            self.login_url = 'base:sinprivilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/home.html'
    login_url = '/login'

class HomeSinPrivilegios(generic.TemplateView):
    template_name = 'base/sin_privilegios.html'