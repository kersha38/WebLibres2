from django.conf.urls import url
from apps.repositorio.views import index,objetoA_view,home

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'objeto', objetoA_view, name='objetoA'),
    url(r'home', home, name='home'),
]