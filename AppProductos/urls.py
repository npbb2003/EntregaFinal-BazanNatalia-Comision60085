from django.urls import path
from AppProductos import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("copiasImpresas/", views.copiasImpresas, name="copias"),
    path(
        "sesionesFotograficas/", views.sesionesFotograficas, name="sesionesFotograficas"
    ),
    path("fotolibros/", views.fotolibros, name="fotolibros"),
    #
    path("busquedaSesiones/", views.busquedaSesiones, name="busquedaSesiones"),
    path("buscar/", views.buscar, name="buscar"),
    #
    path("busquedaCopias/", views.busquedaCopias, name="busquedaCopias"),
    path("buscarCopias/", views.buscarCopias, name="buscarCopias"),
    #
    path("busquedaFotolibros/", views.busquedaFotolibros, name="busquedaFotolibros"),
    path("buscarFotolibros/", views.buscarFotolibros, name="buscarFotolibros"),
    #
    path("lista/", views.CopiasListView.as_view(), name="lista"),
    path("detalle/<int:pk>/", views.CopiasDetalle.as_view(), name="Detail"),
    path("nuevo/", views.CopiasCreateView.as_view(), name="NuevaCopia"),
    path("editar/<int:pk>/", views.CopiasUpdateView.as_view(), name="Edit"),
    path("eliminar/<int:pk>/", views.CopiasDeleteView.as_view(), name="Delete"),
    #
    path("listaSesiones/", views.SesionesListView.as_view(), name="listaSesiones"),
    path(
        "detalleSesion/<int:pk>/",
        views.SesionesDetalle.as_view(),
        name="SesionesDetail",
    ),
    path("nuevaSesion/", views.SesionesCreateView.as_view(), name="NuevaSesion"),
    path(
        "editarSesion/<int:pk>/", views.SesionesUpdateView.as_view(), name="EditSesion"
    ),
    path(
        "eliminarSesion/<int:pk>/",
        views.SesionesDeleteView.as_view(),
        name="DeleteSesion",
    ),
    #
    path("listaFotolibros/", views.FotolibroListView.as_view(), name="listaFotolibros"),
    path(
        "detalleFotolibros/<int:pk>/",
        views.FotolibroDetalle.as_view(),
        name="FotolibrosDetail",
    ),
    path("nuevoFotolibro/", views.FotolibroCreateView.as_view(), name="NuevoFotolibro"),
    path(
        "editarFotolibro/<int:pk>/",
        views.FotolibroUpdateView.as_view(),
        name="EditFotolibro",
    ),
    path(
        "eliminarFotolibro/<int:pk>/",
        views.FotolibroDeleteView.as_view(),
        name="DeleteFotolibro",
    ),
    #
    path("login/", views.login_request, name="Login"),
    path("register/", views.register, name="Register"),
    path(
        "logout/",
        LogoutView.as_view(template_name="appproductos/logout.html"),
        name="Logout",
    ),
]


# path("sesionesFormulario/", views.sesionesFormulario, name="sesionesFormulario"),
# path(
#     "fotolibrosFormulario/", views.fotolibrosFormulario, name="fotolibrosFormulario"
# ),
# path("copiasFormulario/", views.copiasFormulario, name="copiasFormulario"),
# path("leerCopias/", views.leerCopias, name="leerCopias"),
# path("eliminarCopia/<copia_param>", views.eliminarCopia, name="eliminarCopia"),
# path("editarCopia/<copia_param>", views.editarCopia, name="editarCopia"),
