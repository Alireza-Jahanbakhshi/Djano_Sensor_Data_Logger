from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from .serializer import LoginUserSerializer , ChangePasswordSerializer


class UserLogicViewSet(GenericViewSet):

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "err": "parameters did not sent"
            }, status=400)

        data = serializer.validated_data
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if not user:
            return Response({
                "err": "Username or Password wrong"
            }, status=400)
        token = Token.objects.get_or_create(user=user)[0]
        return Response({
            "token": token.key,
        }, status=200)



    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def change_password(self,request):
        """
        """
        serializer = ChangePasswordSerializer(data=request.data , context={"request" : request})
        if not serializer.is_valid():
            return Response({
                "err": serializer.errors
            }, status=400)

        user = serializer.save()
        
        return Response({
            "data" : "password changed"
        },status=400)