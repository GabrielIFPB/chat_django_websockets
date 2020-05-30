
from django.urls import path

from chat.views import Chat, Room

app_name = 'chat'

urlpatterns = [
    path('', Chat.as_view(), name='chat'),
    path('<str:room_name>/', Room.as_view(), name='room'),
]
