# api/admin.py
from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from .models import ApiKey

@admin.register(ApiKey)
class ApiAPIKeyModelAdmin(APIKeyModelAdmin):
    pass


