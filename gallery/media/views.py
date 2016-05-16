from django.shortcuts import render
from django.views.generic import DetailView

from .models import Collection, Item, Share

class UUIDAsIdentifier(object):
    def get_object(self, *args, **kwargs):
        return self.model.objects.get(uuid=self.request.resolver_match.kwargs.get('uuid', None))

class CollectionView(UUIDAsIdentifier, DetailView):
    model = Collection
collection = CollectionView.as_view()

class ItemView(UUIDAsIdentifier, DetailView):
    model = Item
item = ItemView.as_view()

class ShareView(UUIDAsIdentifier, DetailView):
    model = Share
share = ShareView.as_view()
