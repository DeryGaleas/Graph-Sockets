from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from RealGraph import consumer

websocket_urlPattern = {
    path('ws/poldata', consumer.DashConsumer)
}


application = ProtocolTypeRouter({
    # 'http':
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPattern))
    
})