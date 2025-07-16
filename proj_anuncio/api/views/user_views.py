from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.models import User 
from api.serializer import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
# Endpoint de login
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return Response({'message': 'Login realizado com sucesso!'}, status=status.HTTP_200_OK)
        else:
            print(f'Senha incorreta para o usuário: {email}')
            return Response({'message': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        print(f'Usuário não encontrado: {email}')
        return Response({'message': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    data = request.data.copy()
    if 'password' in data:
        data['password'] = make_password(data['password'])
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)  

@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
    data = request.data.copy()
    if 'password' in data:
        data['password'] = make_password(data['password'])
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    user.delete()
    return Response(status=204)