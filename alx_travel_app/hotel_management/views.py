from django.shortcuts import render
from .models import Listing
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ListingSerializer
from rest_framework import viewsets, permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing property listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Optionally filter listings based on query parameters."""
        queryset = Listing.objects.all()

        # Filter by property type
        property_type = self.request.query_params.get('property_type', None)
        if property_type is not None:
            queryset = queryset.filter(property_type=property_type)

        # Filter by minimum price per night
        min_price = self.request.query_params.get('min_price', None)
        if min_price is not None:
            queryset = queryset.filter(price_per_night__gte=min_price)

        # Filter by maximum price per night
        max_price = self.request.query_params.get('max_price', None)
        if max_price is not None:
            queryset = queryset.filter(price_per_night__lte=max_price)

        # Filter by location (case-insensitive search)
        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(location__icontains=location)

        # Filter by minimum number of guests
        max_guests = self.request.query_params.get('max_guests', None)
        if max_guests is not None:
            queryset = queryset.filter(max_guests__gte=max_guests)
        
        # Filter by availability
        is_available = self.request.query_params.get('is_available', None)
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')

        return queryset.order_by('-created_at')  # ← CHANGE THIS LINE

    @action(detail=False, methods=['get'])
    def property_types(self, request):
        """Get all available property types."""
        types = [{'value': key, 'label': label} for key, label in Listing.PROPERTY_TYPES]
        return Response(types)