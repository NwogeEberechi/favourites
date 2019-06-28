from django.db import models
from django.db.models import signals
from .signals import count_changes
from django.utils import	timezone
from django.core.validators import MinLengthValidator

METADATA_TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Data'),
        ('enum', 'Enum'),
    )

class Category(models.Model):
    name =	models.TextField(unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(null=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, default=timezone.now)
    favourite_count = models.IntegerField(default=0, editable=False)

    def	__str__(self):
        return	self.name
    
    def count_changes(self):
        """
        Counts the total number of favourites of this category and saves the result to the `favourite_count` field.
        """
        count = self.favourites.filter(deleted=False).count()
        self.favourite_count = count
        self.save()


class Favourite(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='favourites')
    title =	models.TextField(unique=True)
    description = models.TextField(MinLengthValidator(10, message="Favourite description should not be less than 10 characters"), null=True)
    rank = models.IntegerField(unique=True)
    deleted = models.BooleanField(null=True, default=False)
    created_date = models.DateTimeField(null=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, default=timezone.now)
    
    def	__str__(self):
        return	self.title

class Metadata(models.Model):
    favourite_id = models.ForeignKey(Favourite, on_delete=models.CASCADE, related_name="metadatas")
    name = models.TextField(unique=True)
    value = models.TextField()
    type = models.CharField(max_length=30, choices=METADATA_TYPES)
    created_date = models.DateTimeField(null=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, default=timezone.now)

class Auditlog(models.Model):
    favourite_id = models.ForeignKey(Favourite, on_delete=models.CASCADE, related_name="audit_logs")
    action = models.TextField()
    new_value = models.TextField()
    old_value = models.TextField()
    created_date = models.DateTimeField(null=True, default=timezone.now)

signals.post_save.connect(count_changes, sender=Favourite)
signals.post_delete.connect(count_changes, sender=Favourite)
