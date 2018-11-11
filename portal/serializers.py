from django.contrib.auth.models import User, Group
from api.models import Customer
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30, required=True, allow_blank=True)
    age = serializers.IntegerField(required=True)

    class Meta:
        model = Customer
        fields = "__all__"

