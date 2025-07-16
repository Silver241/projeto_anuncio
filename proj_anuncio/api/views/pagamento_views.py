from backend.models import Pagamento
from api.serializer import PagamentoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    serializer = PagamentoSerializer(pagamentos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_pagamento(request):
    serializer = PagamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_pagamento(request, pk):
    try:
        pagamento = Pagamento.objects.get(pk=pk)
    except Pagamento.DoesNotExist:
        return Response({'error': 'Pagamento not found'}, status=404)

    serializer = PagamentoSerializer(pagamento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_pagamento(request, pk):
    try:
        pagamento = Pagamento.objects.get(pk=pk)
    except Pagamento.DoesNotExist:
        return Response({'error': 'Pagamento not found'}, status=404)

    pagamento.delete()
    return Response(status=204)