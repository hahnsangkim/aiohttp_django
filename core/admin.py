from django.contrib import admin
from core.models import AppConfig, Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(AppConfig)
class AppConfigAdmin(admin.ModelAdmin):
    pass