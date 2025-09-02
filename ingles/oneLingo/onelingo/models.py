from django.db import models

class Base(models.Model):
    dt_criacao = models.DateTimeField('Criação', auto_now_add=True, null=True)
    dt_modificacao = models.DateTimeField('Modificação', auto_now=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Pergunta(Base):
    pergunta = models.CharField('Pergunta', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.pergunta
    
class Resposta(Base):
    resposta = models.CharField('Resposta', max_length=255, null=False, blank=False)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    correto = models.BooleanField('Correta', default=False)

    def __str__(self):
        return self.resposta


class Score(Base):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pontuacao = models.IntegerField('Pontuação', default=0)

    def __str__(self):
        return f"{self.usuario.username} - {self.pergunta.pergunta} - {self.pontuacao}"
    


class Quiz(Base):
    validade = models.DateTimeField('Validade', null=False, blank=False)
    token = models.CharField('Token', max_length=255, null=False, blank=False)
    qtd_respondida = models.IntegerField('Quantidade Respondida', default=0)

    def __str__(self):
        return f"Quiz - {self.id} - {self.validade}"