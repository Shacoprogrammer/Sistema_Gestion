from  django.urls import path
from .views import (
    RegistroUsuarioVista, CustomLoginView, ListaEventosView, DetalleEventoView, CrearEventoView,
    MisEventosView, InscribirEventoView, CustomLogoutView
)

urlpatterns = [
    path('', ListaEventosView.as_view(), name='lista_eventos'),
    path('registro/', RegistroUsuarioVista.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
]