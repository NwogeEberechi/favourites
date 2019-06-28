from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import FavouriteViewSet, CategoryViewSet, MetadataViewSet, CategoryFavouriteViewSet

router = DefaultRouter()
router.register(r'favourite',  FavouriteViewSet, base_name="favourite")
router.register(r'category',  CategoryViewSet, base_name="category")
router.register(r'metadata', MetadataViewSet, base_name="metadata")
# router.register(r'category/favourites', CategoryFavouriteViewSet, base_name="category_favourite")

urlpatterns = [
    # path('favourites', UserArticle.as_view(), name='user_article'),
    path('<int:pk>/favourites', CategoryFavouriteViewSet.as_view(), name='category_favourite'),
]

urlpatterns += router.urls