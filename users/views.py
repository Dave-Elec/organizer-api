from rest_framework import generics, response, status
from . import serializers


class UserRegister(generics.CreateAPIView):
    """
    Register a new `User`.
    """

    serializer_class = serializers.RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            message = "Your account has been created."
            return response.Response(
                data={"data": message},
                status=status.HTTP_201_CREATED,
            )

