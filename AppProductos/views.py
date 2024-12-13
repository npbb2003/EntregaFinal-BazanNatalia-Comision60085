from django.shortcuts import render
from django.http import HttpResponse
from AppProductos.models import SesionFotografica, CopiaImpresa, Fotolibro
from AppProductos.forms import SesionFormulario, CopiaFormulario, FotolibroFormulario
import re
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def inicio(req):

    return render(req, "appproductos/index.html")


def sesionesFotograficas(req):
    return render(req, "appproductos/sesionesFotograficas.html")


def fotolibros(req):

    return render(req, "AppProductos/fotolibros.html")
    # if req.method == "POST":  # Si el formulario fue enviado
    #     miFormulario = FotolibroFormulario(
    #         req.POST
    #     )  # Creamos un objeto formulario con los datos enviados
    #     print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

    #     if miFormulario.is_valid():  # Verificamos si los datos son válidos
    #         informacion = (
    #             miFormulario.cleaned_data
    #         )  # Obtenemos los datos limpios y validados
    #         fotolibro = Fotolibro(
    #             tamanio=informacion["tamaño"],
    #             cant_hojas=informacion["cant_hojas"],
    #             precio=informacion["precio"],
    #         )  # Creamos un objeto Curso
    #         fotolibro.save()  # Guardamos el curso en la base de datos
    #         miFormulario = CopiaFormulario()  # limpiamos el formulario

    # else:
    #     miFormulario = (
    #         FotolibroFormulario()
    #     )  # Creamos un formulario vacío para mostrarlo inicialmente

    # return render(
    #     req,
    #     "AppProductos/fotolibros.html",
    #     {"miFormulario": miFormulario},
    # )


def copiasImpresas(req):

    return render(req, "appproductos/copias.html")

    # if req.method == "POST":  # Si el formulario fue enviado
    #     miFormulario = CopiaFormulario(
    #         req.POST
    #     )  # Creamos un objeto formulario con los datos enviados
    #     print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

    #     if miFormulario.is_valid():  # Verificamos si los datos son válidos
    #         informacion = (
    #             miFormulario.cleaned_data
    #         )  # Obtenemos los datos limpios y validados
    #         copia = CopiaImpresa(
    #             superficie=informacion["superficie"],
    #             tamanio=informacion["tamaño"],
    #             precio=informacion["precio"],
    #         )  # Creamos un objeto Curso
    #         copia.save()  # Guardamos el curso en la base de datos
    #         miFormulario = CopiaFormulario()  # limpiamos el formulario
    # else:
    #     miFormulario = (
    #         CopiaFormulario()
    #     )  # Creamos un formulario vacío para mostrarlo inicialmente

    # return render(req, "appproductos/copias.html", {"miFormulario": miFormulario})

    # # return render(req, "appproductos/copias.html")


def busquedaSesiones(req):
    return render(req, "AppProductos/busquedaSesiones.html")


def buscar(req):
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        lista = SesionFotografica.objects.filter(nombre__icontains=nombre)

        return render(
            req,
            "AppProductos/resultadosBusquedaSesiones.html",
            {"sesiones": lista, "nombre": nombre},
        )

    else:
        respuesta = "Sin datos"
        return HttpResponse(respuesta)


def busquedaCopias(req):
    return render(req, "AppProductos/busquedaCopias.html")


def buscarCopias(req):
    if req.GET["tamanio"]:
        tamanio = req.GET["tamanio"]
        lista = CopiaImpresa.objects.filter(tamanio__icontains=tamanio)

        return render(
            req,
            "AppProductos/resultadosBusquedaCopias.html",
            {"copias": lista, "tamanio": tamanio},
        )

    else:
        respuesta = "Sin datos"
        return HttpResponse(respuesta)


def busquedaFotolibros(req):
    return render(req, "AppProductos/busquedaFotolibros.html")


def buscarFotolibros(req):
    if req.GET["tamanio"]:
        tamanio = req.GET["tamanio"]
        lista = Fotolibro.objects.filter(tamanio__icontains=tamanio)

        return render(
            req,
            "AppProductos/resultadosBusquedaFotolibros.html",
            {"fotolibros": lista, "tamanio": tamanio},
        )

    else:
        respuesta = "Sin datos"
        return HttpResponse(respuesta)


############### vistas basadas en clases ###############
class CopiasListView(ListView):
    """
    Vista para mostrar una lista de todas las copias
    """

    model = CopiaImpresa  # modelo con el que trabaja esta vista

    print(model)

    template_name = (
        "appproductos/copias_list.html"  # plantilla para renderizar la lista
    )


class CopiasDetalle(DetailView):
    """
    Vista para mostrar los detalles de una copia especifica
    """

    model = CopiaImpresa  # modelo con el que trabaja esta vista

    print(model)
    # print(DetailView)
    template_name = (
        "appproductos/copias_detalle.html"  # plantilla para renderizar la lista
    )


class CopiasCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear nuevas copias
    """

    model = CopiaImpresa  # modelo con el que trabaja esta vista
    template_name = (
        "AppProductos/copiasFormulario.html"  # plantilla para renderizar la lista
    )
    success_url = reverse_lazy("lista")  # url de redireccion desp de crear curso
    fields = [
        "superficie",
        "tamanio",
        "precio",
    ]  # campos del modelo a mostrar en el formulario


class CopiasUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar registros de copias a traves de formularios
    """

    model = CopiaImpresa  # modelo con el que trabaja esta vista
    template_name = (
        "AppProductos/copias_edit.html"  # plantilla para renderizar la lista
    )
    # success_url = reverse_lazy("List") #url de redireccion desp de crear curso
    success_url = reverse_lazy(
        "lista"
    )  # otra forma de especificar una url de redireccion

    fields = [
        "superficie",
        "tamanio",
        "precio",
    ]  # campos del modelo a mostrar en el formulario


class CopiasDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminar copias
    """

    model = CopiaImpresa  # modelo con el que trabaja esta vista
    success_url = reverse_lazy(
        "lista"
    )  # url de redireccion para desp de eliminar exitosamente

    template_name = "AppProductos/copias_confirm_delete.html"  # plantilla para confirmar la eliminacion


class SesionesListView(ListView):
    """
    Vista para mostrar una lista de todas las sesiones
    """

    model = SesionFotografica  # modelo con el que trabaja esta vista

    print(model)

    template_name = (
        "appproductos/sesiones_list.html"  # plantilla para renderizar la lista
    )


class SesionesDetalle(DetailView):
    """
    Vista para mostrar los detalles de una sesión especifica
    """

    model = SesionFotografica  # modelo con el que trabaja esta vista

    print(model)
    # print(DetailView)
    template_name = (
        "appproductos/sesiones_detalle.html"  # plantilla para renderizar la lista
    )


class SesionesCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear nuevas sesiones
    """

    model = SesionFotografica  # modelo con el que trabaja esta vista
    template_name = (
        "AppProductos/sesionesFormulario.html"  # plantilla para renderizar la lista
    )
    success_url = reverse_lazy(
        "listaSesiones"
    )  # url de redireccion desp de crear curso
    fields = [
        "nombre",
        "descripcion",
        "precio",
    ]  # campos del modelo a mostrar en el formulario


class SesionesUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar registros de sesiones a traves de formularios
    """

    model = SesionFotografica  # modelo con el que trabaja esta vista
    template_name = (
        "AppProductos/sesiones_edit.html"  # plantilla para renderizar la lista
    )
    # success_url = reverse_lazy("List") #url de redireccion desp de crear curso
    success_url = reverse_lazy(
        "listaSesiones"
    )  # otra forma de especificar una url de redireccion

    fields = [
        "nombre",
        "descripcion",
        "precio",
    ]  # campos del modelo a mostrar en el formulario


class SesionesDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminar sesiones de fotos
    """

    model = SesionFotografica  # modelo con el que trabaja esta vista
    success_url = reverse_lazy(
        "listaSesiones"
    )  # url de redireccion para desp de eliminar exitosamente

    template_name = "AppProductos/sesiones_confirm_delete.html"  # plantilla para confirmar la eliminacion


class FotolibroListView(ListView):
    """
    Vista para mostrar una lista de todas los fotolibros
    """

    model = Fotolibro  # modelo con el que trabaja esta vista

    print(model)

    template_name = (
        "appproductos/fotolibros_list.html"  # plantilla para renderizar la lista
    )


class FotolibroDetalle(DetailView):
    """
    Vista para mostrar los detalles de un fotolibro especifico
    """

    model = Fotolibro  # modelo con el que trabaja esta vista

    print(model)
    # print(DetailView)
    template_name = (
        "appproductos/fotolibros_detalle.html"  # plantilla para renderizar la lista
    )


class FotolibroCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear nuevos fotolibros
    """

    model = Fotolibro  # modelo con el que trabaja esta vista
    template_name = (
        "AppProductos/fotolibrosFormulario.html"  # plantilla para renderizar la lista
    )
    success_url = reverse_lazy(
        "listaFotolibros"
    )  # url de redireccion desp de crear fotolibro
    fields = [
        "tamanio",
        "cant_hojas",
        "precio",
    ]  # campos del modelo a mostrar en el formulario


class FotolibroUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar registros de fotolibros a traves de formularios
    """

    model = Fotolibro  # modelo con el que trabaja esta vista
    template_name = (
        "AppProductos/fotolibro_edit.html"  # plantilla para renderizar la lista
    )

    success_url = reverse_lazy(
        "listaFotolibros"
    )  # otra forma de especificar una url de redireccion

    fields = [
        "tamanio",
        "cant_hojas",
        "precio",
    ]  # campos del modelo a mostrar en el formulario


class FotolibroDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminar fotolibros
    """

    model = Fotolibro  # modelo con el que trabaja esta vista
    success_url = reverse_lazy(
        "listaFotolibros"
    )  # url de redireccion para desp de eliminar exitosamente

    template_name = "AppProductos/fotolibros_confirm_delete.html"  # plantilla para confirmar la eliminacion


############### seccion de logueo ###############
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # si paso la validacion de Django

            usuario = form.cleaned_data.get("username")  # obtiene usuario
            contrasenia = form.cleaned_data.get("password")  # obtiene contraseña

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(
                    request,
                    "appproductos/index.html",
                    {"mensaje": f"Bienvenido {usuario}"},
                )
            else:  # si la autenticacion falla
                form = AuthenticationForm()
                return render(
                    request,
                    "appproductos/index.html",
                    {"mensaje": f"Datos incorrectos", "form": form},
                )
        else:
            return render(
                request, "appproductos/index.html", {"mensaje": f"Formulario Erroneo"}
            )

    form = AuthenticationForm()

    return render(request, "appproductos/login.html", {"form": form})


def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(
                request, "appproductos/index.html", {"mensaje": "Usuario creado"}
            )
    else:
        form = UserRegisterForm()

    return render(request, "appproductos/registro.html", {"form": form})


############### funciones que quedaron sin efecto - IGNORAR ###############


# def fotolibros(req):

#     if req.method == "POST":  # Si el formulario fue enviado
#         miFormulario = FotolibroFormulario(
#             req.POST
#         )  # Creamos un objeto formulario con los datos enviados
#         print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

#         if miFormulario.is_valid():  # Verificamos si los datos son válidos
#             informacion = (
#                 miFormulario.cleaned_data
#             )  # Obtenemos los datos limpios y validados
#             fotolibro = Fotolibro(
#                 tamanio=informacion["tamaño"],
#                 cant_hojas=informacion["cant_hojas"],
#                 precio=informacion["precio"],
#             )  # Creamos un objeto Curso
#             fotolibro.save()  # Guardamos el curso en la base de datos
#             miFormulario = CopiaFormulario()  # limpiamos el formulario

#     else:
#         miFormulario = (
#             FotolibroFormulario()
#         )  # Creamos un formulario vacío para mostrarlo inicialmente

#     return render(
#         req,
#         "AppProductos/fotolibros.html",
#         {"miFormulario": miFormulario},
#     )

# def fotolibrosFormulario(request):
#     if request.method == "POST":  # Si el formulario fue enviado
#         miFormulario = FotolibroFormulario(
#             request.POST
#         )  # Creamos un objeto formulario con los datos enviados
#         print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

#         if miFormulario.is_valid():  # Verificamos si los datos son válidos
#             informacion = (
#                 miFormulario.cleaned_data
#             )  # Obtenemos los datos limpios y validados
#             fotolibro = Fotolibro(
#                 tamanio=informacion["tamanio"],
#                 cant_hojas=informacion["cant_hojas"],
#                 precio=informacion["precio"],
#             )  # Creamos un objeto Curso
#             fotolibro.save()  # Guardamos el curso en la base de datos
#             return render(
#                 request, "AppProductos/index.html"
#             )  # Redirigimos a la página de inicio
#     else:
#         miFormulario = (
#             FotolibroFormulario()
#         )  # Creamos un formulario vacío para mostrarlo inicialmente

#     return render(
#         request,
#         "AppProductos/fotolibrosFormulario.html",
#         {"miFormulario": miFormulario},
#     )

# def leerCopias(req):
#     copias = CopiaImpresa.objects.all()  # trae todas las copias
#     contexto = {"copias": copias}
#     print(contexto)
#     print(copias)
#     return render(req, "AppProductos/leerCopias.html", contexto)


# def eliminarCopia(req, copia_param):

#     print("entra")
#     print(copia_param)
#     print(type(copia_param))

#     # Expresión regular para extraer las partes necesarias
#     patron = r"superficie (.*?), tamaño (.*?) \$([0-9]+)"

#     # Buscar coincidencias
#     resultado = re.search(patron, copia_param)

#     if resultado:

#         copia = CopiaImpresa.objects.get(
#             tamanio=resultado.group(2),
#             superficie=resultado.group(1),
#             precio=int(resultado.group(3)),
#         )
#         print("entra2")
#         if copia:
#             copia.delete()
#         else:
#             print("No hay elementos")
#         print("entra3")
#         # vuelvo al menu
#         copias = CopiaImpresa.objects.all()  # trae todas las copias
#         contexto = {"copias": copias}
#         print(contexto)
#         print(copias)
#     return render(req, "AppProductos/leerCopias.html", contexto)
#     # return 0


# def editarCopia(req, copia_param):

#     # Expresión regular para extraer las partes necesarias
#     patron = r"superficie (.*?), tamaño (.*?) \$([0-9]+)"

#     # Buscar coincidencias
#     resultado = re.search(patron, copia_param)

#     if resultado:

#         copia = CopiaImpresa.objects.get(
#             tamanio=resultado.group(2),
#             superficie=resultado.group(1),
#             precio=int(resultado.group(3)),
#         )
#         print("entra2")
#         if copia:
#             copia.delete()
#         else:
#             print("No hay elementos")
#         print("entra3")
#         # vuelvo al menu
#         copias = CopiaImpresa.objects.all()  # trae todas las copias
#         contexto = {"copias": copias}
#         print(contexto)
#         print(copias)
#     return render(req, "AppProductos/leerCopias.html", contexto)
#     # return 0
