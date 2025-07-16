from backend.models import Minuta
from api.serializer import MinutaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_minutas(request):
    minutas = Minuta.objects.all()
    serializer = MinutaSerializer(minutas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_minuta(request):
    serializer = MinutaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_minuta(request, pk):
    try:
        minuta = Minuta.objects.get(pk=pk)
    except Minuta.DoesNotExist:
        return Response({'error': 'Minuta not found'}, status=404)

    serializer = MinutaSerializer(minuta, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_minuta(request, pk):
    try:
        minuta = Minuta.objects.get(pk=pk)
    except Minuta.DoesNotExist:
        return Response({'error': 'Minuta not found'}, status=404)

    minuta.delete()
    return Response(status=204)