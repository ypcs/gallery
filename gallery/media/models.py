from django.conf import settings
from django.db import models

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField, UUIDField

class Collection(models.Model):
    uuid = UUIDField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=255)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        unique_together = (('owner', 'title',))

    def __str__(self):
        return "{}".format(self.title)
