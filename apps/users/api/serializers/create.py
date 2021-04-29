from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.models import User

duplicate_user = UniqueValidator(queryset=User.objects.all().values('email'),
        message='La dirección de correo electronico que usted ingreso ya existe.')



class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200, validators=[duplicate_user])
    full_name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'description', 'password', 'role', 'token']
        read_only_fields = ('role', 'token')

    def validate(self, data):
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
