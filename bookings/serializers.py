from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(source='property.name', read_only=True)
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['booking_id', 'property', 'property_name', 'user', 'user_name',
                 'start_date', 'end_date', 'total_price', 'status', 'created_at']
        read_only_fields = ['booking_id', 'created_at']