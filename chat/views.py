
from django.views.generic.base import TemplateView


class Chat(TemplateView):
	template_name = 'chat/chat.html'


class Room(TemplateView):
	template_name = 'chat/room.html'
