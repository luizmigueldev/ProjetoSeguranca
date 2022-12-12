from django.db import models
from fernet_fields import EncryptedCharField, EncryptedDateField, EncryptedTextField

class Prontuario(models.Model):
    nome = EncryptedCharField(max_length=255)
    dataNascimento = EncryptedDateField()
    contato = EncryptedCharField(max_length=20)
    pressaoArterial = EncryptedCharField(max_length=10)
    temperatura = EncryptedCharField(max_length=10)
    principaisSintomas = EncryptedTextField()
    dataInternacao = EncryptedDateField()
    dataAlta = EncryptedDateField()
    medicacao = EncryptedTextField()
    observacoesComplementares = EncryptedTextField()

    def __str__(self):
        return self.nome

