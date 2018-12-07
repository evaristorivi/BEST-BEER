from django.contrib.auth.models import User, Group
from rest_framework import serializers
from BBApp.models import *
 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CervezaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cerveza
        fields = ('nombre_cerveza', 'foto')


