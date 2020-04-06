from rest_framework import serializers
from Applications.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'title', 'api_key')

    def create(self, validated_data):
        return Application.objects.create(**validated_data)
