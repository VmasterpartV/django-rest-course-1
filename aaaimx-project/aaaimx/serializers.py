from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User, Division

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = []

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = []

class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        exclude = []
