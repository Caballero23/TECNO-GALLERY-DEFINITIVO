from django import forms
from django.forms import widgets
from .models import Carac_moviles

# Create your models here.


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Carac_moviles
        fields= '__all__'

        