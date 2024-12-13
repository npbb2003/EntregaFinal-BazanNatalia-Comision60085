from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from AppClientes.models import Cliente


def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")


def probando_template(request):

    listaDeNotas = [10, 1, 5, 3, 9]

    nom = "Natalia"
    ap = "Perez"

    diccionario_de_contexto = {
        "nombre": nom,
        "apellido": ap,
        "hoy": datetime.now(),
        "Notas": listaDeNotas,
    }

    # mi_html = open("./EntregaTres/plantillas/template1.html")
    # plantilla = Template(mi_html.read())
    # mi_html.close()
    plantilla = loader.get_template("template1.html")

    # mi_contexto = Context(diccionario_de_contexto)

    # documento = plantilla.render(mi_contexto)
    documento = plantilla.render(diccionario_de_contexto)

    return HttpResponse(documento)


def agregar_cliente(request, nom, ape, edad, email):

    cliente = Cliente(nombre=nom, apellido=ape, edad=edad, email=email)
    cliente.save()
    return HttpResponse("Cliente Agregado")
