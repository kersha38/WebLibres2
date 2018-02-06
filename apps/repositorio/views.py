from django.shortcuts import render, redirect
from apps.repositorio.forms import objetoAForm

# Create your views here.
def index(request):
    return render(request,'repositorio/index.html')

def objetoA_view(request):
    if request.method=='POST':
        form=objetoAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repositorio:index')
    else:
        form=objetoAForm()
    return render(request,'repositorio/objetoA_form.html',{'form':form})