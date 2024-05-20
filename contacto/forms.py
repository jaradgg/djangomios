from django import forms


class FormularioContacto(forms.Form):
    
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    email = forms.EmailField(label="Email",  required=True)
    contenido = forms.CharField(max_length=150, widget=forms.Textarea, label="Contenido", required=True)
    
    
