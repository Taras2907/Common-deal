from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CustomUser


class UsernameIsUsedView(APIView):

    def post(self, request):
        username = request.data['username']
        user_exists = CustomUser.objects.filter(username=username).exists()
        if user_exists:
            return Response({"message": "A user with that username already exists"},
                            status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_200_OK)


class EmailIsUsedView(APIView):

    def post(self, request):
        email = request.data['email']
        email_exists = CustomUser.objects.filter(email=email).exists()
        if email_exists:
            response = {"response": {
                "message": "A user is already registered with this e-mail address.",
                "exists": True,
            }}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {"response": {
                "message": "There is no user with such email.",
                "exists": False,
            }}
            return Response(response, status=status.HTTP_200_OK)
