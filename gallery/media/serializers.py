from rest_framework import serializers
from .models import Collection, Item, Share

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ('uuid', 'owner', 'title', 'status',)
