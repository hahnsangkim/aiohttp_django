from django.urls import path
from . import views as api_view

urlpatterns = [
    path('get_last_active_app_config/', api_view.get_last_active_app_config, name='get-last-active-app-config'),
    path('create_message', api_view.create_message, name='create-message'),
    path('get_message/<int:message_id>/<str:access_token>/', api_view.get_message, name='get-message')
]