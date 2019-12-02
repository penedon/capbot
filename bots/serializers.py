from .models import *
from rest_framework import serializers


class BotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bot
        fields = '__all__'
