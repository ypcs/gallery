from django.conf import settings
from django.db import models

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField, UUIDField

_ = lambda x: x

STATUS_ACTIVE = 'a'
STATUS_INACTIVE = 'i'
STATUS_REMOVED = 'r'

STATUSES = (
    (STATUS_ACTIVE, _('Active')),
    (STATUS_INACTIVE, _('Inactive')),
    (STATUS_REMOVED, _('Removed')),
)

class Collection(models.Model):
    uuid = UUIDField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUS_ACTIVE)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        unique_together = (('owner', 'title',))

    def __str__(self):
        return "{}".format(self.title)

    def has_access(self, user):
        """Checks if user has access to this collection"""
        raise NotImplementedError
