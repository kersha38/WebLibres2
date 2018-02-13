from django.conf.urls import url
from apps.objeto.views import listaObjetos,crearObjeto,editarObjeto,borrarObjeto\
    ,upload_file,download,down2,auto,BuscarView
from django.contrib.auth.decorators import login_required,permission_required

urlpatterns = [
    url(r'listar',listaObjetos.as_view(), name='listaObjetos'),
    url(r'crear',crearObjeto.as_view(), name='creaObjetos'),
    url(r'editar/(?P<pk>\d+)/', editarObjeto.as_view(), name='editaObjetos'),
    url(r'borrar/(?P<pk>\d+)/', borrarObjeto.as_view(), name='borraObjetos'),
    url(r'down/(?P<path>.*)', download, name='down'),
    url(r'down2/(?P<path>.*)', down2, name='down2'),
    url(r'crear2',upload_file, name='creaObj'),
    url(r'buscar',BuscarView.as_view(), name='buscar'),
    url(r'auto',auto, name='autoo'),
]