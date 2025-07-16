from backend.models import Anuncio
from api.serializer import AnuncioSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_anuncios(request):
    anuncios = Anuncio.objects.all()
    serializer = AnuncioSerializer(anuncios, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_anuncio(request):
    serializer = AnuncioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_anuncio(request, pk):
    try:
        anuncio = Anuncio.objects.get(pk=pk)
    except Anuncio.DoesNotExist:
        return Response({'error': 'Anuncio not found'}, status=404)

    serializer = AnuncioSerializer(anuncio, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_anuncio(request, pk):    
    try:
        anuncio = Anuncio.objects.get(pk=pk)
    except Anuncio.DoesNotExist:
        return Response({'error': 'Anuncio not found'}, status=404)

    anuncio.delete()
    return Response(status=204)