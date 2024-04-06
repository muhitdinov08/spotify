from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserUpdatePasswordLinkSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['email']
