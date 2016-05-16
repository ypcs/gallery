from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField, UUIDField
from taggit_machinetags.managers import MachineTaggableManager

_ = lambda x: x

STATUS_ACTIVE = 'a'
STATUS_INACTIVE = 'i'
STATUS_REMOVED = 'r'

STATUSES = (
    (STATUS_ACTIVE, _('Active')),
    (STATUS_INACTIVE, _('Inactive')),
    (STATUS_REMOVED, _('Removed')),
)

SHARE_PUBLIC = 'p'
SHARE_WITH_LINK = 'l'
SHARE_WITH_PASSWORD = 's'
SHARE_WITH_ACCOUNT = 'a'
SHARE_TYPES = (
    (SHARE_PUBLIC, _('Public')),
    (SHARE_WITH_LINK, _('With link')),
    (SHARE_WITH_PASSWORD, _('With Password')),
    (SHARE_WITH_ACCOUNT, _('With Account')),
)

def get_upload_path(instance, filename):
    now = timezone.now()
    return "uploads/{}/{}/{}/{}/{}/{}/{}".format(
            instance.owner,
            now.year,
            now.month,
            now.day,
            "{}{}{}.{}".format(now.hour, now.minute, now.second, now.microsecond),
            instance.uuid,
            filename,
            )

class Collection(models.Model):
    uuid = UUIDField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUS_ACTIVE)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    shares = GenericRelation('media.Share')
    tags = MachineTaggableManager()

    class Meta:
        unique_together = (('owner', 'title',))

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse("media:collection", kwargs={'uuid': self.uuid,})

    def has_access(self, user):
        """Checks if user has access to this collection"""
        raise NotImplementedError

class Item(models.Model):
    uuid = UUIDField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    content = models.FileField(upload_to=get_upload_path)
    content_meta = models.TextField(blank=True, null=True)

    collections = models.ManyToManyField('media.Collection')

    shares = GenericRelation('media.Share')
    tags = MachineTaggableManager()

    def __str__(self):
        return "{}".format(self.uuid)

    def get_absolute_url(self):
        return reverse("media:item", kwargs={'uuid': self.uuid,})

    def create_share(self, owner):
        """Creates new share for Item"""
        share = self.shares.create(owner=owner)
        return share

class Share(models.Model):
    uuid = UUIDField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    status = models.CharField(max_length=1, choices=STATUSES, default=STATUS_ACTIVE)
    share_type = models.CharField(max_length=1, choices=SHARE_TYPES, default=SHARE_WITH_LINK)
    password = models.CharField(max_length=255, blank=True, null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users', blank=True)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    limit = models.Q(app_label='media', model='collection') | models.Q(app_label='media', model='item')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "{}".format(self.uuid)

    def get_absolute_url(self):
        return reverse("media:share", kwargs={'uuid': uuid,})
