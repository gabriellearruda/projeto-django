from rest_framework import serializers
from model import DadosBanco
from django.db.models import Prefetch

class BancoSerializer(serializers.ModelSerializer):
	class Meta:
		model = DadosBanco
		fields = ('pk','host','port','database','username','password','created_at','updated_at')