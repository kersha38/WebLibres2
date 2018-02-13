from django.conf.urls import url
from apps.repositorio.views import index,objetoA_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'objeto', objetoA_view, name='objetoA'),
]