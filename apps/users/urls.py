# Modulos nativos de django
from django.urls import path

# Modulos locales
from apps.users.api.views.login import LoginAPIView
from apps.users.api.views.create import UserCreateAPIView


urlpatterns = [
    path('sing-in/', LoginAPIView.as_view(), name='login'),
    path('sing-up/', UserCreateAPIView.as_view(), name='create'),
]
