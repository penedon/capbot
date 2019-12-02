from .models import *
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'conversationId', 'timestamp',
                  'from', 'to', 'text')

MessageSerializer._declared_fields["from"] = serializers.CharField(source="from_bot")