from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User

class AuthenticationForm(ModelForm):
    
    class Meta:
    
        model = User
        fields = ['username', 'password',]
        widgets = {'password':forms.PasswordInput(),}
        

class PartidoForm(ModelForm):

    class Meta:
    
        model = Partido
        fields = ['nombre',]


class AgrupacionForm(ModelForm):

    class Meta:
    
        model = Agrupacion
        fields = ['nombre', 'ciudad', 'partido']
        
   
class MilitanteForm(ModelForm):

    class Meta:
    
        model = Militante
        fields = ['nombre', 'edad', 'dni', 'agrupacion']
