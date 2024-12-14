from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SesionFormulario(forms.Form):
    """Formulario para ingresar datos de sesiones fotograficas"""

    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=100)
    precio = forms.IntegerField()


class CopiaFormulario(forms.Form):
    """Formulario para ingresar datos de copias impresas de fotografias"""

    superficie = forms.CharField(max_length=40)
    tamaño = forms.IntegerField()
    precio = forms.IntegerField()


class FotolibroFormulario(forms.Form):
    """Formulario para ingresar datos de fotolibros artesanales"""

    tamaño = forms.IntegerField()
    cant_hojas = forms.IntegerField()
    precio = forms.IntegerField()


class buscar(forms.Form):
    """Formulario para ingresar datos en busqueda de sesiones fotograficas"""

    nombre = forms.CharField(max_length=40)


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}


class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput
    )
    # No obligatorios
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "last_name", "first_name"]
        help_texts = {k: "" for k in fields}
