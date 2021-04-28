# Modulos de jwt
import jwt

# Modulos nativos de django
from django.conf import settings

# Modulos locales 
from apps.users.timezone import get_timezone, set_time_expired


def generate_jwt_token(full_name, type_token, role, days=0, minutes=0):
    jwt_token = jwt.encode({
            'name': full_name,
            'token': type_token,
            'role': role,
            'exp': set_time_expired(days=days, minutes=minutes),
            'iat': get_timezone()
        }, settings.SECRET_KEY, algorithm='HS256')

    return jwt_token.decode('utf-8')
