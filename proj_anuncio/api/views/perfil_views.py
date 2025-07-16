from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.models import Perfil 
from api.serializer import PerfilSerializer

@api_view(['GET'])
def get_perfis(request):
    perfis = Perfil.objects.all()
    serializer = PerfilSerializer(perfis, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_perfil(request): 
    serializer = PerfilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_perfil(request, pk):
    try:
        perfil = Perfil.objects.get(pk=pk)
    except Perfil.DoesNotExist:
        return Response({'error': 'Perfil not found'}, status=404)

    serializer = PerfilSerializer(perfil, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_perfil(request, pk): 
    try:
        perfil = Perfil.objects.get(pk=pk)
    except Perfil.DoesNotExist:
        return Response({'error': 'Perfil not found'}, status=404)

    perfil.delete()
    return Response(status=204)