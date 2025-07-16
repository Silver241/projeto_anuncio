from backend.models import Fatura
from api.serializer import FaturaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_faturas(request):
    faturas = Fatura.objects.all()
    serializer = FaturaSerializer(faturas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_fatura(request):
    serializer = FaturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_fatura(request, pk):
    try:
        fatura = Fatura.objects.get(pk=pk)
    except Fatura.DoesNotExist:
        return Response({'error': 'Fatura not found'}, status=404)

    serializer = FaturaSerializer(fatura, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_fatura(request, pk):
    try:
        fatura = Fatura.objects.get(pk=pk)
    except Fatura.DoesNotExist:
        return Response({'error': 'Fatura not found'}, status=404)

    fatura.delete()
    return Response(status=204)
