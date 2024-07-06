from  django.urls import path
from .views import (
    RegistroUsuarioVista, CustomLoginView, ListaEventosView, DetalleEventoView, CrearEventoView,
    MisEventosView, InscribirEventoView, CustomLogoutView
)

urlpatterns = [
    path('', ListaEventosView.as_view(), name='lista_eventos'),
    path('registro/', RegistroUsuarioVista.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('evento/<int:pk>/', DetalleEventoView.as_view(), name='detalle_eventos'),
    path('evento/crear/', CrearEventoView.as_view(), name='crear_eventos'),
    path('mis-eventos/', MisEventosView.as_view(), name='mis_eventos'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('evento/<int:pk>/inscribir/', InscribirEventoView.as_view(), name='inscribir_evento'),

]