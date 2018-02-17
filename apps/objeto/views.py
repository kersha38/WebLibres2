from django.shortcuts import render
from apps.objeto.models import objetoA
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from django.core.urlresolvers import reverse_lazy
from apps.objeto.forms import objetoAForm,archCatForm
from django.http import HttpResponse, Http404
import os
from django.conf import settings
from django.core.files import File
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from bs4 import BeautifulSoup
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import date

# Create your views here.
class listaObjetos(ListView):
    model=objetoA
    template_name='objeto/baseobjeto.html'


class crearObjeto(PermissionRequiredMixin,CreateView):
    permission_required='usuario.esProfesor'
    login_url = reverse_lazy('objetos:listaObjetos')
    model = objetoA
    form_class =objetoAForm
    template_name = 'objeto/objetoA_form.html'
    success_url = reverse_lazy('objetos:listaObjetos')

def upload_file(request):
    if request.method == 'POST':
        form = objetoAForm(request.POST, request.FILES)
        if form.is_valid():
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

def down2(request, path_to_file):
    f = open(path_to_file, 'r')
    myfile = File(f)
    response = HttpResponse(myfile, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + path_to_file
    return response


# cataloga automaticamente
def auto(request):
    if request.method == 'POST':
        form = archCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tituloR=''
            autorR=''
            descripcionR=''
            palabras_claR=''
            fechaR=str(date.today().year)+'-'+str(date.today().month)+'-'+str(date.today().day)
            # archivo html
            archCatR=str(form.cleaned_data['archIndex'])
            archElpR = str(form.cleaned_data['archElp'])

            arch = open(settings.MEDIA_ROOT+'\\archCat\\'+archCatR, 'r')
            contenido = arch.read()
            soup = BeautifulSoup(contenido, "html.parser")

            tituloR=str(soup.title.string)
            print(tituloR)
            for tag in soup.find_all('meta'):

                try:
                    if tag.get('name') == 'author':
                        autorR=tag.get('content')
                        print(autorR)
                except:
                    pass

                try:
                    if tag.get('name') == 'description':
                        descripcionR=tag.get('content')
                        print(descripcionR)
                        break
                except:
                    pass
            for cla in tituloR.split(' '):
                palabras_claR+=cla.strip('\n')
            arch.close()

            # inserto nuevo Objeto
            foo_instance = objetoA.objects.create(
                nombre=tituloR
                , descripcion=descripcionR,
                autor=autorR,
                institucion='EPN',
                fechaCreacion=fechaR,
                fechaIngreso=fechaR,
                palabras_clave=palabras_claR,
                archivo=archElpR)

            # foo_instance.save()

            object_list2=objetoA.objects.all()
            return render(request, 'objeto/baseobjeto.html', {'object_list': object_list2})
    else:
        form = archCatForm()
    return render(request, 'objeto/archCat_form.html', {'form': form})


# busco objetos por tema o nombre, tags o descripcion
class BuscarView(TemplateView):

    def post(self, request, *args,**kwargs):
        buscado=request.POST['buscado']
        object_list = objetoA.objects.filter(Q(nombre__icontains=buscado)
                                             |Q(palabras_clave__icontains=buscado)
                                             | Q(tema__Nombre_tema__icontains=buscado)
                                             | Q(descripcion__icontains=buscado)
                                             | Q(autor__icontains=buscado))


        return render(request,'objeto/baseobjeto.html',{'object_list':object_list})