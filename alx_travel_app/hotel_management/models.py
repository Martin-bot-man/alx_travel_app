from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Listing(models.Model):
    """
    Model representing a property listing.
    """
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('condo', 'Condo')
    ]
    
    # Basic Information
    title = models.CharField(
        max_length=200,
        help_text="Property title/name"
    )
    description = models.TextField(
        help_text="Detailed description of the property"
    )
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES,
        help_text="Type of property"
    )
    
    # Pricing
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Price per night in USD"
    )
    
    # Location
    location = models.CharField(
        max_length=100,
        help_text="Property location (city, country)"
    )
    
    # Capacity
    max_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Maximum number of guests"
    )
    
    # Amenities
    amenities = models.JSONField(
        default=list,
        blank=True,
        help_text="List of amenities (e.g., WiFi, Pool, Parking)"
    )
    
    # Timestamps (RECOMMENDED - tracks when created/updated)
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when listing was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when listing was last updated"
    )
    
    # Availability (OPTIONAL - useful feature)
    is_available = models.BooleanField(
        default=True,
        help_text="Whether the property is available for booking"
    )
    
    # Owner (OPTIONAL - if you want to track who created the listing)
    # Uncomment if you want this feature
    # owner = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='listings',
    #     null=True,
    #     blank=True,
    #     help_text="User who created this listing"
    # )
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name = 'Property Listing'
        verbose_name_plural = 'Property Listings'
        indexes = [
            models.Index(fields=['property_type']),
            models.Index(fields=['location']),
            models.Index(fields=['price_per_night']),
        ]
    
    def __str__(self):
        """String representation of the listing."""
        return f"{self.title} - {self.get_property_type_display()} in {self.location}"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"<Listing: {self.id} - {self.title}>"
    
    @property
    def amenities_count(self):
        """Returns the number of amenities."""
        return len(self.amenities) if self.amenities else 0
    
    def get_price_range(self):
        """Categorize property by price range."""
        if self.price_per_night < 100:
            return "Budget"
        elif self.price_per_night < 250:
            return "Standard"
        elif self.price_per_night < 500:
            return "Premium"
        else:
            return "Luxury"
    
    def clean(self):
        """Custom validation."""
        from django.core.exceptions import ValidationError
        
        if self.price_per_night <= 0:
            raise ValidationError("Price per night must be greater than 0")
        
        if self.max_guests < 1:
            raise ValidationError("Maximum guests must be at least 1")
        
        if not isinstance(self.amenities, list):
            raise ValidationError("Amenities must be a list")