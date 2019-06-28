from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Favourite, Category, Metadata
from .serializers import FavouriteSerializer, CategorySerializer, MetadataSerializer

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryFavouriteViewSet(ListAPIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        queryset = category.favourites.all()
        data = FavouriteSerializer(queryset, many=True).data
        return Response(data)

class MetadataViewSet(viewsets.ModelViewSet):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer
