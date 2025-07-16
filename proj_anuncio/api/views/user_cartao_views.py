from backend.models import UserCartao
from api.serializer import UserCartaoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_user_cartoes(request):
    user_cartoes = UserCartao.objects.all()
    serializer = UserCartaoSerializer(user_cartoes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user_cartao(request):
    serializer = UserCartaoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_user_cartao(request, pk):
    try:
        user_cartao = UserCartao.objects.get(pk=pk)
    except UserCartao.DoesNotExist:
        return Response({'error': 'UserCartao not found'}, status=404)

    serializer = UserCartaoSerializer(user_cartao, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_user_cartao(request, pk):
    try:
        user_cartao = UserCartao.objects.get(pk=pk)
    except UserCartao.DoesNotExist:
        return Response({'error': 'UserCartao not found'}, status=404)

    user_cartao.delete()
    return Response(status=204)