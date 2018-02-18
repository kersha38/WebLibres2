from django.conf.urls import url
from apps.objeto.views import listaObjetos,crearObjeto,editarObjeto,borrarObjeto\
    ,upload_file,download,down2,auto,BuscarView\
    ,nuevocoment,listaCo
from django.contrib.auth.decorators import login_required,permission_required

urlpatterns = [
    url(r'listar',login_required(listaObjetos.as_view()), name='listaObjetos'),
    url(r'crear',login_required(crearObjeto.as_view()), name='creaObjetos'),
    url(r'editar/(?P<pk>\d+)/', login_required(editarObjeto.as_view()), name='editaObjetos'),
    url(r'borrar/(?P<pk>\d+)/', login_required(borrarObjeto.as_view()), name='borraObjetos'),
    url(r'down/(?P<path>.*)', login_required(download), name='down'),
    url(r'down2/(?P<path>.*)', login_required(down2), name='down2'),
    url(r'crear2',login_required(upload_file), name='creaObj'),
    url(r'buscar',login_required(BuscarView.as_view()), name='buscar'),
    url(r'auto',login_required(auto), name='autoo'),

    url(r'coment/(?P<id_objeto>\d+)/$',login_required(nuevocoment) , name='newComent'),
    url(r'listComent/(?P<id_objeto>\d+)/$',login_required(listaCo), name='listaComents'),
]