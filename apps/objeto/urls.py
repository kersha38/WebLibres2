from django.conf.urls import url
from apps.objeto.views import listaObjetos,crearObjeto,editarObjeto,borrarObjeto,upload_file

urlpatterns = [
    url(r'listar', listaObjetos.as_view(), name='listaObjetos'),
    url(r'crear', crearObjeto.as_view(), name='creaObjetos'),
    url(r'editar/(?P<pk>\d+)/', editarObjeto.as_view(), name='editaObjetos'),
    url(r'borrar/(?P<pk>\d+)/', borrarObjeto.as_view(), name='borraObjetos'),
]