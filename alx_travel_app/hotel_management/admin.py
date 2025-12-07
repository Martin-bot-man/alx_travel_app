from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Listing model.
    Provides a powerful interface for managing property listings.
    """
    
    # Fields to display in the list view
    list_display = [
        'id',
        'title',
        'property_type',
        'price_per_night',
        'location',
        'max_guests',
        'is_available',
        'created_at',
        'amenities_count_display'
    ]
    
    # Fields that are clickable links to detail view
    list_display_links = ['id', 'title']
    
    # Add filters in the right sidebar
    list_filter = [
        'property_type',
        'is_available',
        'created_at',
        'max_guests',
    ]
    
    # Add search functionality
    search_fields = [
        'title',
        'description',
        'location',
    ]
    
    # Fields that can be edited directly in list view
    list_editable = [
        'is_available',
        'price_per_night',
    ]
    
    # Default ordering (newest first)
    ordering = ['-created_at']
    
    # Number of items per page
    list_per_page = 25
    
    # Organize fields in the detail/edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'property_type')
        }),
        ('Pricing & Capacity', {
            'fields': ('price_per_night', 'max_guests')
        }),
        ('Location & Availability', {
            'fields': ('location', 'is_available')
        }),
        ('Amenities', {
            'fields': ('amenities',),
            'classes': ('collapse',),  # Collapsible section
            'description': 'Enter amenities as a JSON list, e.g., ["WiFi", "Pool", "Parking"]'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    # Make timestamp fields read-only
    readonly_fields = ['created_at', 'updated_at']
    
    # Add date hierarchy navigation
    date_hierarchy = 'created_at'
    
    # Custom method to display amenities count
    def amenities_count_display(self, obj):
        """Display the number of amenities."""
        count = obj.amenities_count
        if count == 0:
            return "No amenities"
        elif count == 1:
            return "1 amenity"
        else:
            return f"{count} amenities"
    
    amenities_count_display.short_description = 'Amenities'
    
    # Custom actions
    actions = ['make_available', 'make_unavailable', 'duplicate_listing']
    
    def make_available(self, request, queryset):
        """Mark selected listings as available."""
        updated = queryset.update(is_available=True)
        self.message_user(
            request,
            f'{updated} listing(s) marked as available.'
        )
    make_available.short_description = "Mark selected as available"
    
    def make_unavailable(self, request, queryset):
        """Mark selected listings as unavailable."""
        updated = queryset.update(is_available=False)
        self.message_user(
            request,
            f'{updated} listing(s) marked as unavailable.'
        )
    make_unavailable.short_description = "Mark selected as unavailable"
    
    def duplicate_listing(self, request, queryset):
        """Duplicate selected listings."""
        count = 0
        for listing in queryset:
            listing.pk = None  # Remove primary key
            listing.title = f"{listing.title} (Copy)"
            listing.save()
            count += 1
        
        self.message_user(
            request,
            f'{count} listing(s) duplicated successfully.'
        )
    duplicate_listing.short_description = "Duplicate selected listings"
    
    # Override save method to add custom logic if needed
    def save_model(self, request, obj, form, change):
        """
        Custom save logic.
        Add any custom behavior when saving through admin.
        """
        # Example: Auto-set owner if you add that field later
        # if not change:  # Only on creation
        #     obj.owner = request.user
        
        super().save_model(request, obj, form, change)
    
    # Customize the admin interface appearance
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)  # Optional: custom CSS
        }
        js = ('admin/js/custom_admin.js',)  # Optional: custom JavaScript


# Alternative: Simple registration (if you don't need all the features above)
# admin.site.register(Listing)