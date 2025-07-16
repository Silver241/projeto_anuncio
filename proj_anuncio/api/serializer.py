from rest_framework import serializers  
from backend.models import Perfil, User, Minuta, Anuncio, Pagamento, Fatura, Cartao, UserCartao

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MinutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minuta
        fields = '__all__'


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'


class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = '__all__'

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = '__all__'


class UserCartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartao
        fields = '__all__'
