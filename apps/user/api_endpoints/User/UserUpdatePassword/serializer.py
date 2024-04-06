from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserPasswordUpdateSerializer(ModelSerializer):
    password1 = CharField(max_length=123)
    password2 = CharField(max_length=123)

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError("password1 and password2 must match")
        return attrs

    def update(self, instance, validated_data):
        instance.password1 = validated_data.get("password1", instance.password1)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['password1']
