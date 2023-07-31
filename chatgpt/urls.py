from django.urls import path
from django.conf import settings
from . import views

app_name = 'chatgpt'

urlpatterns = [
    path('', views.ChatAPI.as_view(), name='chat'),
]
