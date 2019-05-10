from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import path, re_path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

#from chatconsumers import ChatConsumer
from chat.consumers import ChatConsumer



application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(

        URLRouter(
            [
                re_path(r"^messages/(?P<username>[\w.@+-]+)", ChatConsumer),
            ]
        )

    )
})
#r"^messages/(?P<username>[\w.@+-]+)/$"