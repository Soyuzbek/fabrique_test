from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from accounts.serializers import TokenObtainPairResponseSerializer, TokenRefreshResponseSerializer


class TokenViewSet(ViewSetMixin,
                   GenericAPIView):
    www_authenticate_realm = 'api'

    def get_serializer_class(self):
        if self.action == 'create':
            return TokenObtainPairSerializer
        if self.action == 'refresh':
            return TokenRefreshSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer})
    def create(self, request, *args, **kwargs):
        return self.token_semi_mixin(request, *args, **kwargs)

    @action(['post'], False)
    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenRefreshResponseSerializer})
    def refresh(self, request, *args, **kwargs):
        return self.token_semi_mixin(request, *args, **kwargs)

    def token_semi_mixin(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )
