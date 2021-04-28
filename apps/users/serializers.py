from rest_framework import serializers 
from rest_framework.exceptions import AuthenticationFailed

# Modulos nativos de django
from django.contrib.auth import authenticate

from .models import User
from .timezone import get_timezone

 

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)
    

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'token']
        read_only_fields = ('token', 'full_name',)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        
        validate_account = User.objects.filter(email=email).first()
        
        """
        Antes de que un usuario se autentique se debera validar algunos datos.
        1. Que la dirección de correo electronico exista.
        2. Que la cuenta del usuario se encuentre activa.


        """
        
        if validate_account is None:
            msg = 'La dirección de correo elctronico que usted ingreso no existe.'
            raise AuthenticationFailed(msg)
        
        if not validate_account.is_active:
            msg = 'La cuenta a la que intenta iniciar sesión fue desactivada.'
            raise AuthenticationFailed(msg)


        """
        Si las validaciones anteriores fueron superadas ahora se debe de validar.
        1. Que las credenciales de autenticación sean las correctas.
        2. Con el metodo save, actualizamos los tokens siempre y cuando hayan caducado.


        """
        user = authenticate(username=email, password=password)
         
        if user is None:
            msg = 'Dirección de correo electronico y/o contraseña incorrecta.'
            raise AuthenticationFailed(msg)


        user.last_login = get_timezone()
        user.save()
        

        return {
            'email': user.email,
            'full_name': user.full_name,
            'token': user.token
        }




    
