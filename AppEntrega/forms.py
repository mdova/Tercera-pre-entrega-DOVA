from django import forms
from datetime import date

class ProveedoresFormulario(forms.Form):
    empresa = forms.CharField(max_length=30)
    cuit = forms.IntegerField()
    localidad = forms.CharField(max_length=50)

class VendedoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    activo_actualmente = forms.BooleanField(required=False)

class ProductosFormulario(forms.Form):
    sku = forms.IntegerField()
    descripcion = forms.CharField(max_length=50)
    fecha = forms.DateField(initial= date.today())
    disponibilidad = forms.BooleanField(required=False)
