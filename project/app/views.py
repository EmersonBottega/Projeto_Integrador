from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Participante
from .serializers import ParticipanteSerializer
from rest_framework.permissions import AllowAny  # Permissão para acesso sem autenticação
from django.shortcuts import render

def home(request):
    return render(request, 'index.html') 

def cadastro_view(request):
    return render(request, 'index_cad.html')

def sucess_page(request):
    return render(request, 'index_sucess.html')

def participante_page(request):
    return render(request, 'index_participante.html')

def perfil_view(request):
    user = request.user  # O usuário autenticado
    try:
        # Busca o participante relacionado ao usuário logado
        participante = Participante.objects.get(usuario=user)  
    except Participante.DoesNotExist:
        participante = None  # Se não existir, define como None

    return render(request, 'perfil.html', {'user': user, 'participante': participante})

class ParticipanteListView(APIView):
    permission_classes = [AllowAny]  # Permite acesso a todos
    
    def get(self, request):
        participantes = Participante.objects.all()
        serializer = ParticipanteSerializer(participantes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("Dados recebidos:", request.data)  # Verifique o que está sendo recebido
        serializer = ParticipanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipanteDetailView(APIView):
    permission_classes = [AllowAny]  # Permite acesso a todos

    def get(self, request, pk):
        participante = get_object_or_404(Participante, pk=pk)
        serializer = ParticipanteSerializer(participante)
        return Response(serializer.data)

    def put(self, request, pk):
        participante = get_object_or_404(Participante, pk=pk)
        serializer = ParticipanteSerializer(participante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        participante = get_object_or_404(Participante, pk=pk)
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
