from django.shortcuts import get_object_or_404, redirect, render, HttpResponse 

from moviles.models import Carac_moviles, Fundas, Protector 
from .forms import ProductoForm 
from django.views.generic import ListView
from django.contrib import messages
# Create your views here.
html_base = """
<h1>MI WEB DE MÓVILES</h1>
<ul>
<li><a href="/">Portadas</a></li>
<li><a href="/moviles/">Acerca de</a></li>
<li><a href="/accesorios/">Portafolio</a></li>
<li><a href="/contact/">Contacto</a></li>


</ul>
"""
def home(request):
    return render(request ,"vistas/home.html")


def moviles(request):

    moviles=Carac_moviles.objects.all()
    

    return render(request ,"vistas/moviles.html", {"moviles": moviles})


def accesorios(request):

    fundas = Fundas.objects.all()
    protector =Protector.objects.all()

    return render(request ,"vistas/accesorios.html", {'fundas': fundas , 'protector' : protector})

def contact(request):

    
    return render(request ,"vistas/contact.html")


def donde_estamos(request):
    return render(request ,"vistas/donde_estamos.html")


def añadir(request):

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje para informar éxito redirección
            messages.add_message(request, 
                messages.SUCCESS, 
                'Equipo creado.')
            return redirect('/')
    else:
        form = ProductoForm()
    datos = {'form': ProductoForm()}
    return render(request, "vistas/añadir.html", 
        context=datos)
    



def buscamoviles(request):
    return render(request ,"vistas/buscamoviles.html")


class SearchResultsListView(ListView):
    model = Carac_moviles
    context_object_name = 'Carac_moviles'
    template_name = 'buscamoviles.html'  # No usará la plantilla estándar del ListView

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Carac_moviles.objects.filter(nombre__icontains=query)
        return []  # cuando entramos a buscar o si no se introduce nada




def modificar(request, id):

    movil =get_object_or_404(Carac_moviles,id=id)

    data={
        'form': ProductoForm(instance=movil)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=movil, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="moviles")
        data["form"] = formulario


    return render(request, 'vistas/modificar.html', data)



def eliminar(request, id):
    movil =get_object_or_404(Carac_moviles,id=id)
    movil.delete()
    return redirect(to="moviles")


