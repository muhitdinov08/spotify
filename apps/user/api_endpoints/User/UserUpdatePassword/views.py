from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from apps.user.api_endpoints.User.UserUpdatePassword.serializer import UserPasswordUpdateSerializer
from apps.user.models import User


class UserUpdatePasswordViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer


__all__ = ['UserUpdatePasswordViewSet']