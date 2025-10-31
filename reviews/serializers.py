from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(source='property.name', read_only=True)
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = Review
        fields = ['review_id', 'property', 'property_name', 'user', 'user_name',
                 'rating', 'comment', 'created_at']
        read_only_fields = ['review_id', 'created_at']