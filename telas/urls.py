from django.urls import path
from . import views
from .views import ProntuarioCreate, ProntuarioUpdate, ProntuarioDelete

urlpatterns = [
    path('', views.index),
    path('criarProntuario/', ProntuarioCreate.as_view(), name='criar_prontuario'),
    path('editarProntuario/<int:pk>/', ProntuarioUpdate.as_view(), name='editar_prontuario'),
    path('excluirProntuario/<int:pk>/', ProntuarioDelete.as_view(), name='excluir_prontuario'),
    path('listaProntuario/', views.lista_prontuario, name='lista_prontuario'),
    path('<int:prontuario_id>', views.visualisar_prontuario, name='visualisar_prontuario'),
]