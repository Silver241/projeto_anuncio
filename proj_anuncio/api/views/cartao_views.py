from backend.models import Cartao
from api.serializer import CartaoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def get_cartoes(request):
    cartoes = Cartao.objects.all()
    serializer = CartaoSerializer(cartoes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_cartao(request):
    serializer = CartaoSerializer(data=request.data)
    if serializer.is_valid():
        data = request.data.copy()
        campos_cartao = ['numero', 'nome', 'MM', 'YY', 'CVV']
        for campo in campos_cartao:
            if campo in data:
                data[campo] = make_password(data[campo])
        serializer = CartaoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_cartao(request, pk):
    try:
        cartao = Cartao.objects.get(pk=pk)
    except Cartao.DoesNotExist:
        return Response({'error': 'Cartao not found'}, status=404)

    data = request.data.copy()
    campos_cartao = ['numero', 'nome', 'MM', 'YY', 'CVV']
    for campo in campos_cartao:
        if campo in data:
            data[campo] = make_password(data[campo])

    serializer = CartaoSerializer(cartao, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_cartao(request, pk):
    try:
        cartao = Cartao.objects.get(pk=pk)
    except Cartao.DoesNotExist:
        return Response({'error': 'Cartao not found'}, status=404)

    cartao.delete()
    return Response(status=204)