from rest_framework import serializers
from .models import Collection, Item, Share

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Collection
        fields = ('uuid', 'owner', 'title', 'status',)

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Item
        fields = ('uuid', 'owner',)
