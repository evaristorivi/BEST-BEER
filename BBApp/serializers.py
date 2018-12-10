from django.contrib.auth.models import User, Group
from rest_framework import serializers
from BBApp.models import *
 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')




class CervezaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cerveza
        fields = '__all__'


class PubsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pub
        fields = '__all__'

class VotacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votaciones
        fields = '__all__'


        

