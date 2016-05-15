from django.contrib import admin
from .models import Collection, Item

class CollectionAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('title', 'uuid', 'owner', 'status',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'owner',)

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Item, ItemAdmin)
