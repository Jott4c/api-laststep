from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .models import User

from .permissions import IsAdminOrAuthenticated


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def patch(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
