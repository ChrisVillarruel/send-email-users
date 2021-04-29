from django.core.mail import send_mail
from django.conf import settings


def get_admin(self):
    """
    Obtenemos el email del administrador


    """
    return self.Meta.model.objects.filter(role='Administrador').values('email')


def send_email(full_name, email, admin):
    """
    Enviamos un correo al administrador utilizando el servidor de correos EMAIL_HOST_USER


    """


    send_mail(f'El cliente {full_name.upper()} a olvidado su contraseña',
        f'Su dirección de correo electronico es: {email}. Haga caso omiso de este mensaje si no es insistente.',
        settings.EMAIL_HOST_USER, # remitente
        [admin[0]['email']], # destinatario
        fail_silently=False) # Si hay algun error no lo silencies

    return None
