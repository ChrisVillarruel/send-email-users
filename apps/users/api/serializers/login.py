
# Modulos rest_framework
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

# Modulos nativos de django
from django.contrib.auth import authenticate

# Modulos locales
from apps.users.models import User
from apps.users.timezone import get_timezone
from apps.users.send_email import send_email, get_admin




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

        """
        Antes de que un usuario se autentique se debera validar algunos datos.
        1. Que la dirección de correo electronico exista.
        2. Que la cuenta del usuario se encuentre activa.


        """
        
        user_exists = self.Meta.model.objects.filter(email=email).first()

        if user_exists is None:
            msg = 'La dirección de correo elctronico que usted ingreso no existe.'
            raise AuthenticationFailed(msg)

        if not user_exists.is_active:
            msg = 'La cuenta a la que intenta iniciar sesión fue desactivada.'
            raise AuthenticationFailed(msg)


        """
        Si las validaciones anteriores fueron correctas ahora se debe de validar.

        1. Que las credenciales de autenticación sean las correctas.
        2. Si el usuario no ingresa bien su contraseña el sistema de manera automatica
           enviara un correo al administrador del sistema que se le notificara que o
           bien alguien ajeno quiere acceder o al cliente se le olvido la contraseña.

           ya dependera del administrador resetear la contraseña o no.

        3. Y con el metodo save, actualizamos los tokens siempre y cuando hayan caducado.


        """

        user = authenticate(username=email, password=password)


        if user is None:
            if user_exists.role == 'Cliente':
                send_email(user_exists.full_name, user_exists, get_admin(self))
 
                msg = 'Si se le olvido su contraseña, ya se le notifico al administrador para investigar su caso. De lo contrario intente de nuevo iniciar sesión.'
                raise AuthenticationFailed(msg)


            msg = 'Dirección de correo electronico y/o contraseña incorrecta.'
            raise AuthenticationFailed(msg)


        user.last_login = get_timezone()
        user.save()


        return {
            'email': user.email,
            'full_name': user.full_name,
            'token': user.token
        }





