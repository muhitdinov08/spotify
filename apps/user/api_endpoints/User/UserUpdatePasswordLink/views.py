import os

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.api_endpoints.User.UserUpdatePasswordLink.serializer import UserUpdatePasswordLinkSerializer
from apps.user.api_endpoints.User.UserUpdatePasswordLink.tasks import send_email


class UserUpdatePasswordLink(APIView):
    def post(self, request):
        serializer = UserUpdatePasswordLinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        host_email = os.getenv("EMAIL_HOST_USER")
        activation_link = f"http://localhost:8000/api/v1/user/user-update-password/{request.user.token}"
        message = render_to_string("activation_link.html",
                                   {"email": serializer.validated_data.get("email"),
                                    "activation_link": activation_link})

        send_email(subject="Activation Link", message=strip_tags(message),
                   from_email=host_email, recepient_list=[request.user.userprofile.email])
        serializer.is_valid()
        return Response(data={'detail': "Check your inbox we have sent an password update link"})


__all__ = ['UserUpdatePasswordLink']
