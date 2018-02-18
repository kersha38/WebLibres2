from django.conf.urls import url
from apps.repositorio.views import index,objetoA_view,home,herramienta
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'objeto', login_required(objetoA_view), name='objetoA'),
    url(r'home', login_required(home), name='home'),
    url(r'herramienta', login_required(herramienta), name='herramienta'),
]