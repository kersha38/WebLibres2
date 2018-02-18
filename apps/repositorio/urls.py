from django.conf.urls import url
from apps.repositorio.views import index,objetoA_view,home,herramienta

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'objeto', objetoA_view, name='objetoA'),
    url(r'home', home, name='home'),
    url(r'herramienta', herramienta, name='herramienta'),
]