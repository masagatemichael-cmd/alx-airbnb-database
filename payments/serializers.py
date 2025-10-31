from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    booking_info = serializers.CharField(source='booking.booking_id', read_only=True)
    
    class Meta:
        model = Payment
        fields = ['payment_id', 'booking', 'booking_info', 'amount', 
                 'payment_method', 'payment_date']
        read_only_fields = ['payment_id', 'payment_date']