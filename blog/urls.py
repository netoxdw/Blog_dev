from django.urls import path
from .views import IndexView, GeneralesView, YacimientosView, PerforacionView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('general', GeneralesView.as_view(), name='generales'),
    path('yacimiento', YacimientosView.as_view(), name='yacimientos'),
    path('perforacion', PerforacionView.as_view(), name='perforacion'),
]