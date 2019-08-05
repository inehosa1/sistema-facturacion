from django.urls import path
from inv.views import (
    CategiaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategiaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel,
    MarcaView, MarcaNew, MarcaEdit, marca_inactiva, UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidadmedida_inactiva,
    ProductoView, ProductoNew ,ProductoEdit, producto_inactiva
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
    path('marca/del/<int:id>', marca_inactiva, name="marca_inactivar"),

    path('unidadmedida/', UnidadMedidaView.as_view(), name="unidadmedida_list"),
    path('unidadmedida/new/', UnidadMedidaNew.as_view(), name="unidadmedida_new"),
    path('unidadmedida/edit/<int:pk>', UnidadMedidaEdit.as_view(), name="unidadmedida_edit"),
    path('unidadmedida/del/<int:id>', unidadmedida_inactiva, name="unidadmedida_inactivar"),

    path('producto/', ProductoView.as_view(), name="producto_list"),
    path('producto/new/', ProductoNew.as_view(), name="producto_new"),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name="producto_edit"),
    path('producto/del/<int:id>', producto_inactiva, name="producto_inactivar")


]
