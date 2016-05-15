from django.contrib import admin
from .models import Collection, Item, Share

class CollectionAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('title', 'uuid', 'owner', 'status',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'owner',)

class ShareAdmin(admin.ModelAdmin):
    list_filter = ('content_type', 'status',)
    list_display = ('content_object', 'uuid', 'owner', 'status',)

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Share, ShareAdmin)
