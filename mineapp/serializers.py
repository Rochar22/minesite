from rest_framework import serializers

class PasswordCheckSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
