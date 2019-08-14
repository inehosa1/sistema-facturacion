from django.urls import path
from base.views import Home, HomeSinPrivilegios
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/login.html'), name="logout"),  
    path('sinprivilegios/', HomeSinPrivilegios.as_view(), name="sinprivilegios")    
]
