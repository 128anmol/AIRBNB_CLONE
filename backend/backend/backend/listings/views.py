from rest_framework import viewsets
from .models import Listing, Booking, Favorite
from .serializers import ListingSerializer, BookingSerializer, FavoriteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_bookings(self, request):
        user = request.user
        bookings = Booking.objects.filter(user=user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer