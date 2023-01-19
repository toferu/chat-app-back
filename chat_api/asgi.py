"""
ASGI config for chat_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import chat.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.routing import get_default_application
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_api.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
            chat.routing.websocket_urlpatterns 
            )
        )    
    ),
})
        
# application = get_default_application()
