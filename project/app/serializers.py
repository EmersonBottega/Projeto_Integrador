from .models import Participante, Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'sexo', 'senha']
        extra_kwargs = {
            'senha': {'write_only': True}  # A senha será write-only
        }

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está cadastrado.")
        return value

    def validate_senha(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value

class ParticipanteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Participante
        fields = ['usuario']  # Incluindo apenas a chave estrangeira do Usuario

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        participante = Participante.objects.create(usuario=usuario)
        return participante
