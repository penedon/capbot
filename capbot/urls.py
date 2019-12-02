from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from bots import views as bots_views
from bot_messages import views as messages_views

router = routers.DefaultRouter()
router.register('bots', bots_views.BotViewSet)
router.register('messages', messages_views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
