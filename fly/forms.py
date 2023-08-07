
from django import forms

class CalulatorForm2(forms.Form):
 
    Precio_de_compra_producto = forms.IntegerField(initial=100)