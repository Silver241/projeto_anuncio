from rest_framework import serializers  
from backend.models import Perfil, User, Minuta, Anuncio, Pagamento, Fatura, Cartao, UserCartao

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    perfil = serializers.CharField(source='perfil_id.tipo', read_only=True)
    perfil_id = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all(), write_only=True)

    class Meta:
        model = User
        fields = ['id', 'perfil', 'perfil_id', 'nome', 'email', 'telefone', 'password']



class MinutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minuta
        fields = '__all__'


from rest_framework import serializers
from backend.models import Anuncio, User

class AnuncioSerializer(serializers.ModelSerializer):
    minuta_tipo = serializers.CharField(source='minuta_id.tipo', read_only=True)  # Exibe o tipo da minuta
    minuta_id = serializers.PrimaryKeyRelatedField(
        queryset=Anuncio._meta.get_field('minuta_id').remote_field.model.objects.all(),
        write_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )

    class Meta:
        model = Anuncio
        fields = [
            'id',
            'minuta_tipo',   # só leitura, aparece no GET
            'minuta_id',     # write_only
            'user_id',       # write_only
            'nome',
            'email',
            'telefone',
            'regiao',
            'canal',
            'horario',
            'vezes',
            'conteudo',
            'estado'
        ]
        extra_kwargs = {
            'minuta_id': {'write_only': True},
            'user_id': {'write_only': True},
        }





class PagamentoSerializer(serializers.ModelSerializer):
    data_pagamento = serializers.DateField(read_only=True)
    anuncio_conteudo = serializers.CharField(source='anuncio_id.conteudo', read_only=True) 
    anuncio_nome = serializers.CharField(source='anuncio_id.nome', read_only=True)  # Exibe o nome do anúncio
    anuncio_id = serializers.PrimaryKeyRelatedField(
        queryset=Anuncio.objects.all(),
        write_only=True
    )
    cartao_id = serializers.PrimaryKeyRelatedField(
        queryset=Cartao.objects.all(),
        write_only=True
    )

    class Meta:
        model = Pagamento
        fields = [
            'id',
            'anuncio_id',
            'cartao_id',
            'valor_total',
            'anuncio_nome',  
            'anuncio_conteudo',  
            'metodo_pagamento',
            'data_pagamento',
        ]
        extra_kwargs = {
            'anuncio_id': {'write_only': True},
            'cartao_id': {'write_only': True},
        }


class FaturaSerializer(serializers.ModelSerializer):
    pagamento = serializers.CharField(source='pagamento_id.valor_total', read_only=True)

    class Meta:
        model = Fatura
        fields = ['id', 'numero_recibo', 'pagamento']

class CartaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cartao
        fields = '__all__'


class UserCartaoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user_id.nome', read_only=True)
    cartao = serializers.CharField(source='cartao_id.numero', read_only=True)

    class Meta:
        model = UserCartao
        fields = ['id', 'user', 'cartao']

