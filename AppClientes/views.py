from django.shortcuts import render
from AppClientes.models import Cliente
from django.http import HttpResponse

# Create your views here.


def cliente(self):
    cliente = Cliente(
        nombre="Natalia", apellido="Bazan", edad=42, email="naty.bazan@gmail.com"
    )
    cliente.save()

    documento = (
        f"Cliente: {cliente.nombre}, edad: {cliente.edad}, email: {cliente.email}"
    )

    return HttpResponse(documento)
