from django.db import models
from django.utils import	timezone
from django.core.validators import MinLengthValidator

METADATA_TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Data'),
        ('enum', 'Enum'),
    )

class Category(models.Model):
    name =	models.TextField()
    description = models.TextField()
    created_date = models.DateTimeField(null=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, default=timezone.now)

    def	__str__(self):
        return	self.name


class Favourite(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title =	models.TextField()
    description = models.TextField(MinLengthValidator(10, message="Favourite description should not be less than 10 characters"), null=True)
    rank = models.IntegerField()
    deleted = models.BooleanField(null=True, default=False)
    created_date = models.DateTimeField(null=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, default=timezone.now)
    
    def	__str__(self):
        return	self.title

class Metadata(models.Model):
    favourite = models.ForeignKey(Favourite, on_delete=models.CASCADE, related_name="favourite")
    name = models.TextField()
    value = models.TextField()
    type = models.CharField(max_length=30, choices=METADATA_TYPES)
    created_date = models.DateTimeField(null=True, default=timezone.now)
    modified_date = models.DateTimeField(null=True, default=timezone.now)

class Auditlog(models.Model):
    favourite = models.ForeignKey(Favourite, on_delete=models.CASCADE, related_name="favourite_item")
    author = models.TextField()
    new_value = models.TextField()
    old_value = models.TextField()
    created_date = models.DateTimeField(null=True, default=timezone.now)
