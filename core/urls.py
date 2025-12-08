from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistroListView.as_view(), name='home'),
    path('crear/', views.RegistroCreateView.as_view(), name='registro_create'),
    path('editar/<int:pk>/', views.RegistroUpdateView.as_view(), name='registro_update'),
    path('eliminar/<int:pk>/', views.RegistroDeleteView.as_view(), name='registro_delete'),
]
