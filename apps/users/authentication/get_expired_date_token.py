# modulos nativos de django
from django.conf import settings


# Modulos de jwt
import jwt

# Modulos de python
from datetime import datetime

# Modulos locales
from apps.users.timezone import get_timezone



def get_expired_date_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
        
        """ Obtenemos el timepo de expiración del token y le restamos cinco dias  """
        get_date_expired = payload['exp'] - 432000
        return datetime.fromtimestamp(get_date_expired).strftime('%y%m%d')
        
    except jwt.exceptions.SignatureExpiredError as e:
        """ Si el token ya expiro entoces retorna la fecha actual en el formato %y%m%d  """
        return get_timezone().strftime('%y%m%d')


