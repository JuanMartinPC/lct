from random import choices
from click import option
from django import forms
from .models import Productos

Empresas = [
    ("Natura", "Natura"), 
    ("Millanel", "Millanel"), 
    ("Tupper", "Tupper"), 
    ("Winnem", "Winnem"), 
    ("Avon", "Avon"), 
    ("MeryKay", "MeryKay")
    ]

class ProductosForm(forms.ModelForm):

    class Meta:
        model=Productos
        fields = ["nombre", "codigo", "stock", "precio", "descripcion", "img", "empresa"]

        
