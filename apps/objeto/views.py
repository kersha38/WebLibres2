from django.shortcuts import render
from apps.objeto.models import objetoA
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.objeto.forms import objetoAForm
from django.http import HttpResponse, Http404
import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required


# Create your views here.
class listaObjetos(ListView):
    model=objetoA
    template_name='objeto/baseobjeto.html'

    class meta:
        permissions=(('esProfe','Da permiso de profesor'),
                     ('esAlumno','Da permiso de alumno'))

#@permission_required('repositorio.esProfe')
class crearObjeto(CreateView):
    model = objetoA
    form_class =objetoAForm
    template_name = 'objeto/objetoA_form.html'
    success_url = reverse_lazy('objetos:listaObjetos')

def upload_file(request):
    if request.method == 'POST':
        form = objetoAForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return reverse_lazy('objetos:listaObjetos')
    else:
        form = objetoAForm()
    return render(request, 'objeto/objetoA_form.html', {'form': form})

class editarObjeto(UpdateView):
    model= objetoA
    form_class = objetoAForm
    template_name = 'objeto/objetoA_form.html'
    success_url = reverse_lazy('objetos:listaObjetos')

class borrarObjeto(DeleteView):
    model=objetoA
    template_name = 'objeto/borrarObj.html'
    success_url = reverse_lazy('objetos:listaObjetos')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404