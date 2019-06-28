from django.db.models import signals
from django.dispatch import dispatcher

def count_changes(sender, instance, signal, *args, **kwargs):
  """
  Runs through all the categories and adds up their current numbers
  """
  from .models import Category
  for category in Category.objects.all():
    category.count_changes()