from django.db import models

# PERFIL (user, super_user, admin)
class Perfil(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo


# USER
class User(models.Model):
    perfil_id = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)  # com hash

    def __str__(self):
        return self.nome


# MINUTA
class Minuta(models.Model):
    tipo = models.CharField(max_length=100)
    conteudo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tipo


# ANUNCIO
class Anuncio(models.Model):
    minuta_id = models.ForeignKey(Minuta, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    regiao = models.CharField(max_length=20, choices=[
        ('Barlavento', 'Barlavento'),
        ('Sotavento', 'Sotavento')
    ])
    
    canal = models.CharField(max_length=10, choices=[
        ('RCV', 'RCV'),
        ('RCV+', 'RCV+'),
        ('TCV', 'TCV')
    ])
    
    horario = models.CharField(max_length=10, choices=[
        ('12:30', '12:30'),
        ('18:30', '18:30')
    ])
    
    vezes = models.IntegerField(choices=[
        (1, '1 vez'),
        (2, '2 vezes'),
        (3, '3 vezes'),
        (4, '4 vezes'),
        (5, '5 vezes')
    ])
    conteudo = models.TextField()
    
    estado = models.CharField(max_length=20, choices=[
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído')
    ])

    def save(self, *args, **kwargs):
        if self.user_id:
            self.nome = self.user_id.nome
            self.email = self.user_id.email
            self.telefone = self.user_id.telefone
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id.nome} - {self.minuta_id.tipo}" if self.user_id else "Anúncio"


# CARTAO
class Cartao(models.Model):
    numero = models.CharField(max_length=255, null=False, blank=False, default='', db_column='numero')
    nome = models.CharField(max_length=255, null=False, blank=False, default='', db_column='nome')
    MM = models.CharField(max_length=255, null=False, blank=False, default='', db_column='MM')  # mês
    YY = models.CharField(max_length=255, null=False, blank=False, default='', db_column='YY')  # ano
    CVV = models.CharField(max_length=255, null=False, blank=False, default='', db_column='CVV')

    def __str__(self):
        return f"{self.nome} - ****{self.numero[-4:]}"


# PAGAMENTO
class Pagamento(models.Model):
    anuncio_id = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    cartao_id = models.ForeignKey(Cartao, on_delete=models.SET_NULL, null=True)
    valor_total = models.FloatField()
    metodo_pagamento = models.CharField(max_length=50)
    data_pagamento = models.DateField(auto_now_add=True) 

    def __str__(self):
        return f"Pagamento de {self.valor_total}€"


# FATURA
class Fatura(models.Model):
    pagamento_id = models.OneToOneField(Pagamento, on_delete=models.CASCADE)
    numero_recibo = models.CharField(max_length=100)

    def __str__(self):
        return f"Fatura #{self.numero_recibo}"


# user_cartao – relacionamento N:N entre User e Cartao
class UserCartao(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cartao_id = models.ForeignKey(Cartao, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'cartao_id')
