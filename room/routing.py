from django.urls import path
#from django.urls import re_path
from . import consumers


websocket_urlpatterns=[
	path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
	#path(r'ws/room/(?P<str:room_name>)/$',consumers.ChatConsumer.as_asgi()),
]