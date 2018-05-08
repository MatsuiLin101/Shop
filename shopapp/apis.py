from . import models, serializers

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ShopappViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticated,)
