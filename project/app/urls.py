from django.urls import path
from .views import home, cadastro_view, sucess_page, participante_page, perfil_view, ParticipanteListView, ParticipanteDetailView

urlpatterns = [
    path('', home, name='home'),  # A homepage será acessada através da raiz do site
    path('cadastro/', cadastro_view, name='cadastro'),
    path('sucesso/', sucess_page, name='sucesso'),
    path('participantes/', ParticipanteListView.as_view(), name='participante-list'),  # Endpoint para listar e cadastrar participantes
    path('participante/', participante_page, name='participante'), 
    path('perfil/', perfil_view, name='perfil'),
    path('participantes/<int:pk>/', ParticipanteDetailView.as_view(), name='participante-detail'),  # atualizar e deletar um participante
]



