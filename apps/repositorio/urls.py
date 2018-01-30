from django.conf.urls import url
from apps.repositorio.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]