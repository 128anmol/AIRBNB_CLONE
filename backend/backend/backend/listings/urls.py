from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]