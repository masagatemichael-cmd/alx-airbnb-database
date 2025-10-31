import graphene
import graphene_django
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from properties.models import Property
from bookings.models import Booking
from payments.models import Payment
from reviews.models import Review

# User Type
class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at')

# Property Type
class PropertyType(DjangoObjectType):
    class Meta:
        model = Property
        fields = '__all__'

# Booking Type
class BookingType(DjangoObjectType):
    class Meta:
        model = Booking
        fields = '__all__'

# Payment Type
class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment
        fields = '__all__'

# Review Type
class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = '__all__'

# Query Class
class Query(graphene.ObjectType):
    # User queries
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, user_id=graphene.String())
    
    # Property queries
    all_properties = graphene.List(PropertyType)
    property_by_id = graphene.Field(PropertyType, property_id=graphene.String())
    properties_by_location = graphene.List(PropertyType, location=graphene.String())
    
    # Booking queries
    all_bookings = graphene.List(BookingType)
    booking_by_id = graphene.Field(BookingType, booking_id=graphene.String())
    
    # Payment queries
    all_payments = graphene.List(PaymentType)
    
    # Review queries
    all_reviews = graphene.List(ReviewType)
    reviews_by_property = graphene.List(ReviewType, property_id=graphene.String())

    # Resolver methods
    def resolve_all_users(self, info):
        return get_user_model().objects.all()
    
    def resolve_user_by_id(self, info, user_id):
        return get_user_model().objects.get(user_id=user_id)
    
    def resolve_all_properties(self, info):
        return Property.objects.all()
    
    def resolve_property_by_id(self, info, property_id):
        return Property.objects.get(property_id=property_id)
    
    def resolve_properties_by_location(self, info, location):
        return Property.objects.filter(location__icontains=location)
    
    def resolve_all_bookings(self, info):
        return Booking.objects.all()
    
    def resolve_booking_by_id(self, info, booking_id):
        return Booking.objects.get(booking_id=booking_id)
    
    def resolve_all_payments(self, info):
        return Payment.objects.all()
    
    def resolve_all_reviews(self, info):
        return Review.objects.all()
    
    def resolve_reviews_by_property(self, info, property_id):
        return Review.objects.filter(property_id=property_id)

# Mutation for creating properties
class CreateProperty(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        location = graphene.String(required=True)
        price_per_night = graphene.Decimal(required=True)
    
    property = graphene.Field(PropertyType)
    
    def mutate(self, info, name, description, location, price_per_night):
        property = Property(
            name=name,
            description=description,
            location=location,
            price_per_night=price_per_night,
            host=info.context.user
        )
        property.save()
        return CreateProperty(property=property)

# Mutation class
class Mutation(graphene.ObjectType):
    create_property = CreateProperty.Field()

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)