
# Modulos de rest_framework
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

# Modulos locales
from apps.users.api.serializers.create import CreateUserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

