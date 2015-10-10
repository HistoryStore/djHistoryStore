__author__ = 'richpolis'
#To change this template use Tools | Templates.
from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('id','name','image_url')