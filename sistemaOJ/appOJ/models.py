from django.db import models
import uuid

class Usuario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    alergias = models.TextField(blank=True, null=True)
    qr_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()
    data_atividade = models.DateTimeField()
    colaborador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='atividades_colaboradas')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Presenca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='presencas')
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='presencas')
    data_presenca = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Presença: {self.usuario.nome} - {self.atividade.nome}'

class Certificado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='certificados')
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='certificados')
    data_emissao = models.DateField(auto_now_add=True)
    horas_participacao = models.PositiveIntegerField()

    def __str__(self):
        return f'Certificado: {self.usuario.nome} - {self.atividade.nome}'
    