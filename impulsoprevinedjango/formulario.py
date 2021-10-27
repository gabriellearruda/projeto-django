# -*- encoding:utf-8 -*-
from django import forms
# adicionado
from django.forms import ModelForm, Form
from django.contrib.auth.models import User, Permission
from django.db.models import Q
from django.forms.models import BaseModelFormSet, BaseInlineFormSet, BaseFormSet
from django.conf import settings

class DadosBanco(forms.Form):
    host = forms.CharField(required=True, max_length=255, label='Host', widget=forms.TextInput(attrs={'class': 'form-control'}))
    port = forms.CharField(required=True, max_length=128, label='Port', widget=forms.TextInput(attrs={'class': 'form-control'}))
    database = forms.CharField(required=True, max_length=128, label='Database', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, max_length=128, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, max_length=128, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))