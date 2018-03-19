from rest_framework import serializers
from backend.views import *
from backend.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    cinemas = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'cinemas')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class FilmOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmOffice
        fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = ('url', 'name', 'address', 'price', 'brand', 'region', 'filmOffice', 'createUser', 'createTime', 'modifyTime')
