from django.shortcuts import render
from .models import Listing
from rest_framework .decorators import action
from rest_framework.response import Response
from .serializers import ListingSerializer
from rest_framework import viewsets, permissions, status



# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    """ViewSet for Listing model providing CRUD operation.
    list:Get all Listings
    create: create a new Listing
    update: Update a Listing
    patrial_update: Partially update a Listing(PATCH)
    destroy: Delete a Listing"""

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Optionally filter listings based on query parameters."""
        queryset =Listing.objects.all()

        #filter by availability
        is_available = self.request.query_params.get('is_available', None)
        if is_available is not None:
            queryset = queryset.filter(is_available= is_available.lower() == 'true')

        min_price = self.request.query_params.get('min_price', None)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        max_price = self.request.query_params.get('max_price', None)
        if max_price is not None:
            queryset =queryset.filter(price__lte=max_price)  

        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset =queryset.filter(location__icontains=location)

        return queryset.order_by('-created_at')   

    def perform_create(self, serializer):
        '''Set the owner to the current user when creating a listing. '''
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def bookings(self, request, pk = None):
        """Custom action to get all bookings for a specific listing.
         URL: /api/listings/{id}/bookings/ """  
        listing = self.get_object()
        bookings = listing.bookings.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)  


class BookingViewSet(viewsets.ModelViewSet):
    '''ViewSet for Booking model providing CRUD operations.
    list: Get all Bookings
    create: Create a new Booking
    retrieve: Get a specific Booking by ID
    update: update a Booking(PUT)
    partial_update: Partially update a booking(PATCH)
    destroy: Delete a booking'''

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        '''Optionally filter listings based on query parameters.'''
        queryset = Listing.objects.all()

        #filter by property type
        property_type = self.request.query_params.get('property_type', None)
        if property_type is not None:
            queryset = queryset.filter(property_type=property_type)

        min_price = self.request.query_params.get('min_price', None)
        if min_price is not None:
            queryset =queryset.filter(price_per_night__gte=min_price)

        max_price = self.request.query_params.get('max_price', None)
        if max_price is not None:
            queryset =queryset.filter(price_per_night__lte=max_price)

        location = self.request.query_params.get('location', None)  
        if location is not None:
            queryset =queryset.filter(location__icontains=location)

        max_guests = self.request.query_params.get('max_guests', None)
        if max_guests is not None:
            queryset =queryset.filter(max_guests__gte=max_guests)    


        return queryset.order_by('-id')

