from django.shortcuts import render
from apps.usuario.models import RegistroUsuario
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import registroForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail


# Create your views here.
class registroUser(CreateView):
    model = RegistroUsuario
    form_class =registroForm
    template_name = 'usuario/registro_form.html'
    success_url = reverse_lazy('login')

def login2(request):
    return reverse_lazy('objetos:listaObjetos')

def crearUsuario(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            form.save()

            # creo usuario
            usernameR=str(form.cleaned_data['username'])
            first_nameR = str(form.cleaned_data['nombre'])
            last_nameR = str(form.cleaned_data['apellido'])
            emailR = str(form.cleaned_data['email'])
            clave=str(get_random_string(length=10))
            passwordR=make_password(clave)

            foo_instance = User.objects.create(
                username=usernameR
            ,first_name=first_nameR,
            last_name=last_nameR,
            email=emailR, password=passwordR)

            # enlazar registroUsuario y usuario
            ru=RegistroUsuario.objects.get(username=usernameR)
            us=User.objects.get(username=usernameR)
            ru.user=us
            ru.save()

            # enviar mail
            msg='Hola su registro ha sido completado\n' \
                'su clave es: '+clave+\
                '\n su usuario es: '+usernameR
            send_mail(
                'Credenciales Repositorio',
                msg,
                'proyecto.libres001@gmail.com',
                [emailR],
                fail_silently=False,
            )

            return render(request, 'index.html')
    else:
        form = registroForm
    return render(request, 'usuario/registro_form.html', {'form': form})