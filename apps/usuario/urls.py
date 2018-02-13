from django.conf.urls import url
from apps.usuario.views import registroUser,crearUsuario,login2


urlpatterns = [
    url(r'registrar', crearUsuario, name='crearU'),
    url(r'login2', login2, name='login2'),
]