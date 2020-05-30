
from django.views.generic.base import TemplateView


class Chat(TemplateView):
	template_name = 'chat/chat.html'


class Room(TemplateView):
	template_name = 'chat/room.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context
