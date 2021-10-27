# -*- encoding:utf-8 -*-
from django.db import models


class DadosBanco(models.Model):
	host = models.CharField(max_length=128)
	port = models.CharField(max_length=128)
	database = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	password = models.CharField(max_length=1028)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + u'-' + self.config.name

	class Meta:
		app_label = 'bancodedados'