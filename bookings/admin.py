from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'property', 'user', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['property__name', 'user__email']