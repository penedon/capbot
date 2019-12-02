from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class MessageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer
    # pagination_class = BillPagination
    model = Message
    queryset = Message.objects.all()
    filter_backends = (DjangoFilterBackend,
                    #    filters.SearchFilter,
                    #    filters.OrderingFilter
                      )
    filterset_fields = ('conversationId',)
    http_method_names = ['get', 'post']
    # search_fields = ('reference',)