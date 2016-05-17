from django.shortcuts import render
from django.views.generic import DetailView

from rest_framework import viewsets

from .models import Collection, Item, Share
from .permissions import IsOwnerOrShared
from .serializers import CollectionSerializer, ItemSerializer

class UUIDAsIdentifier(object):
    def get_object(self, *args, **kwargs):
        return self.model.objects.get(uuid=self.request.resolver_match.kwargs.get('uuid', None))

class CollectionView(UUIDAsIdentifier, DetailView):
    model = Collection
collection = CollectionView.as_view()

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'uuid'
    permission_classes = (IsOwnerOrShared,)

class ItemView(UUIDAsIdentifier, DetailView):
    model = Item
item = ItemView.as_view()

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'uuid'
    permission_classes = (IsOwnerOrShared,)

class ShareView(UUIDAsIdentifier, DetailView):
    model = Share
share = ShareView.as_view()
