from .consumers import *
from django.urls import path
websocket_urlpatterns = [

    path('ws/sc/', MyCon.as_asgi()),
]