from rest_framework import serializers as srz


class TokenObtainPairResponseSerializer(srz.Serializer):
    access = srz.CharField()
    refresh = srz.CharField()


class TokenRefreshResponseSerializer(srz.Serializer):
    access = srz.CharField()
