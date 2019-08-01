from django.urls import path
from inv.views import (
    CategiaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategiaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel,
    MarcaView, MarcaNew, MarcaEdit, MarcaDel
)

urlpatterns = [
    path('categorias/', CategiaView.as_view(), name="categoria_list"),
    path('categorias/new/', CategoriaNew.as_view(), name="categoria_new"),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name="categoria_edit"), 
    path('categorias/del/<int:pk>', CategoriaDel.as_view(), name="categoria_del"),

    path('subcategorias/', SubCategiaView.as_view(), name="subcategoria_list"),
    path('subcategorias/new/', SubCategoriaNew.as_view(), name="subcategoria_new"),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name="subcategoria_edit"),
    path('subcategorias/del/<int:pk>', SubCategoriaDel.as_view(), name="subcategoria_del"),

    path('marca/', MarcaView.as_view(), name="marca_list"),
    path('marca/new/', MarcaNew.as_view(), name="marca_new"),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name="marca_edit"),
    path('marca/del/<int:pk>', MarcaDel.as_view(), name="marca_del"),

]
