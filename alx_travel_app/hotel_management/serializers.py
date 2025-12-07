from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    
    property_type_display = serializers.CharField(
        source='get_property_type_display', 
        read_only=True
    )
    
    # Add computed fields
    amenities_count = serializers.ReadOnlyField()
    price_range = serializers.SerializerMethodField()
    
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'property_type',
            'property_type_display',
            'price_per_night',
            'price_range',
            'location',
            'max_guests',
            'amenities',
            'amenities_count',
            'is_available',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_price_range(self, obj):
        """Get the price range category."""
        return obj.get_price_range()