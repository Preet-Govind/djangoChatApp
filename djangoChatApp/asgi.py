import os
#import django
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoChatApp.settings')
#django.setup()
# application = get_asgi_application()
application=ProtocolTypeRouter({
	"http" : get_asgi_application(),
	"websocket" : AuthMiddlewareStack(
		URLRouter(
				room.routing.websocket_urlpatterns
			)
		)
})
