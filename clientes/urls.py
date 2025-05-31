from django.urls import path
from . import views


app_name = "clientes"

urlpatterns = [
    path ("", views.clientes_home, name="home"),
    path ("adicionar/", views.clientes_adicionar, name="adicionar" ),
    path("registrar_desempenho/<int:id>", views.registrar_desempenho, name='registrar_desempenho'),
    path ("desempenho/<int:id>", views.clientes_desempenho, name="desempenho" ),
    path ("remover/<int:id>", views.clientes_remover, name= "remover"),
    path ("editar/<int:id>", views.clientes_editar, name="editar")
]
