from django.urls import path
from .views import IndexView, YacimientosView, PerforacionView, ProduccionView, PostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produccion', ProduccionView.as_view(), name='produccion'),
    path('yacimiento', YacimientosView.as_view(), name='yacimientos'),
    path('perforacion', PerforacionView.as_view(), name='perforacion'),
    path('<str:categoria>/<str:slug>/', PostView.as_view(), name='post-detail'),
]