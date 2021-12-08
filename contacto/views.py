from django.shortcuts import redirect, render

from .forms import Formulario
# Create your views here.

def contacto(request):

    Formulario_Contacto = Formulario()
    
    if request.method=="POST":
        Formulario_Contacto=Formulario(data=request.POST)
        if Formulario_Contacto.is_valid():
            nombre=request.POST.get("nombre") 
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/?valido")



    return render(request ,"contacto/contact.html" , {'Formulario' : Formulario_Contacto})
