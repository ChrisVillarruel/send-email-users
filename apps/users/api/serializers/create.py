
# modulos de rest_framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Modulos locales
from apps.users.models import User


""" Validamo que la dirección de correo electronico no exista  """
duplicate_user = UniqueValidator(queryset=User.objects.all().values('email'),
        message='La dirección de correo electronico que usted ingreso ya existe.')


def test(value):
    if value.isnumeric():
        msg = 'Los caracteres numericos no son validos dentro de este campo.'
        raise serializers.ValidationError(msg)
    


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200, validators=[duplicate_user])
    full_name = serializers.CharField(max_length=200, validators=[test])
    description = serializers.CharField(max_length=250, validators=[test])
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'description', 'password', 'role', 'token']
        read_only_fields = ('role', 'token')

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
