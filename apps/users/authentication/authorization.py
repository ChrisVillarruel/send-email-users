# Modulos de django
from django.conf import settings

# Modulos de rest_framework 
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

# Modulos de JWT
import jwt

# Modulos locales
from apps.users.models import User


class JWTAuthentication(BaseAuthentication):
    prefix_header_authentication = 'Bearer'


    def authenticate(self, request):
        request.user = None

        auth_header = get_authorization_header(request).split()
        auth_prefix_header = self.prefix_header_authentication.lower()

        if not auth_header:
            """ 
            Si la cabecera de autenticación es false, quiere decir que ningun usuario esta autenticado.
            retornamos None, pues el inicio de sesión no requeire de un token de acceso
            

            """

            return None

        if len(auth_header) == 1:
            msg = 'No se ha proveeido un token de autenticación.'
            raise AuthenticationFailed(msg)

        if len(auth_header) > 2:
            msg = 'Token invalido y/o contiene errores ortografico.'
            raise AuthenticationFailed(msg)



        """ Decodificamos el auth header utilizando el estandar utf-8  """
        prefix = auth_header[0].decode('utf-8')
        jwt_token = auth_header[1].decode('utf-8')


        if prefix.lower() != auth_prefix_token:
            msg = 'El prefijo de autenticación no es el esperado.'
            raise AuthenticationFailed(msg)


        """
        Si la autenticación por token supero todas las validaciones
        quiere decir que el token es valido y es un token codificado en jwt.
        Ahora solo falta validar las credenciales del token y si el token fue firmado
        por el sistema.


        """

        return self._authenticate_credentials(request, jwt_token)



        def _authenticate_credentials(self, request, jwt_token):
            try:
                """ Decodificamos el token """
                payload = jwt.decode(jwt_token, settigs.SECRET_KEY)

                """ Obtenemos el tipo de token que se decodifico  """
                token_type = payload['token']

                """ Dependiendo del token validamos que exista en la base de datos """
                if token_type == 'access_token':
                    user = User.objects.get(access_token=jwt_token)

                if token_type == 'refresh_token':
                    user = User.objects.get(refresh_token=jwt_token)

                if not user.is_active:
                    msg = 'El usuario al que intentas autenticarte se encuentra baneado del sistema.'
                    raise AuthenticationFailed(msg)

            except jwt.ExpiredSignatureError as e:
                msg = 'El token de autenticación ha expirado.'
                raise AuthenticationFailed(msg)

            except jwt.exceptions.DecodeError as e:
                msg = 'Ocurrio un error al decoficar el token.'
                raise AuthenticationFailed(msg)

            except user.DoesNotExist as e:
                msg = 'El token de autenticación no existe o fue eliminado.'
                raise AuthenticationFailed(msg)


            return (user, token)










