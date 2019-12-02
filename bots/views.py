from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class BotViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = BotSerializer
    # pagination_class = BillPagination
    model = Bot
    queryset = Bot.objects.all()
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter,
    #                    filters.OrderingFilter)
    # filterset_fields = ('company__uniqueName', 'reference',)
    # search_fields = ('reference',)
