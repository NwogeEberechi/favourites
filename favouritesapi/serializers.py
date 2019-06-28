from rest_framework import serializers

from .models import Favourite, Category, Metadata

class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ('id', 'category_id', 'title', 'description', 'rank', 'deleted', 'created_date', 'modified_date')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_date', 'modified_date', 'favourite_count')

class MetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metadata
        fields = ('id', 'favourite_id', 'name', 'value', 'type', 'created_date', 'modified_date')