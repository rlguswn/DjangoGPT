from django.urls import path
from django.conf import settings
from .views import ChatView

app_name = 'chatgpt'

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
]
