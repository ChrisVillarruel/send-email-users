from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):
    """ Creamos el manager para la reación de usuarios y administradores  """

    def create_user(self, email, full_name, description, password=None):
        if email is None:
            raise TypeError('Asegurese de haber ingresado su dirección de correo electronico.')

        if full_name is None:
            raise TypeError('Asegurese de haber ingresado su nombre y apellidos.')

        user = self.model(email=self.normalize_email(email), full_name=full_name.title(), description=description)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, full_name, description,  password):

        if password is None:
            raise TypeError('Asegurese de habe ingresado una contraseña')

        user = self.create_user(email, full_name, description,  password)

        user.is_superuser = True
        user.is_staff = True
        user.save()


        return user






