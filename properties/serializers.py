from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    host_name = serializers.CharField(source='host.get_full_name', read_only=True)
    
    class Meta:
        model = Property
        fields = ['property_id', 'host', 'host_name', 'name', 'description', 
                 'location', 'price_per_night', 'created_at', 'updated_at']
        read_only_fields = ['property_id', 'created_at', 'updated_at']