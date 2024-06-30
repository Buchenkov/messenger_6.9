"""
ASGI config for messenger_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from messenger_app import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messenger_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path('ws/chat/<str:chat_name>/', consumers.ChatConsumer.as_asgi()),
            ]
        )
    ),
})
