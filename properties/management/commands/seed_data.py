from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from properties.models import Property
from bookings.models import Booking
from reviews.models import Review
from decimal import Decimal
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample Airbnb data'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Check if we already have users
        if User.objects.filter(role='host').exists():
            self.stdout.write(
                self.style.WARNING('Sample data already exists. Skipping.')
            )
            return

        self.stdout.write('Creating sample data...')

        try:
            # Create host users
            host1 = User.objects.create_user(
                email='john@example.com',
                password='password123',
                first_name='John',
                last_name='Smith',
                role='host'
            )
            
            host2 = User.objects.create_user(
                email='sarah@example.com', 
                password='password123',
                first_name='Sarah',
                last_name='Johnson',
                role='host'
            )
            
            # Create guest user
            guest = User.objects.create_user(
                email='mike@example.com',
                password='password123',
                first_name='Mike',
                last_name='Brown',
                role='guest'
            )

            # Create properties
            property1 = Property.objects.create(
                host=host1,
                name='Cozy Downtown Apartment',
                description='Beautiful apartment in city center',
                location='New York',
                price_per_night=Decimal('120.00')
            )
            
            property2 = Property.objects.create(
                host=host1,
                name='Beach House',
                description='Amazing beachfront property',
                location='Miami', 
                price_per_night=Decimal('200.00')
            )
            
            property3 = Property.objects.create(
                host=host2,
                name='Mountain Cabin',
                description='Peaceful retreat in the mountains',
                location='Colorado',
                price_per_night=Decimal('95.00')
            )

            # Create a booking
            booking = Booking.objects.create(
                property=property1,
                user=guest,
                start_date=datetime.now().date() + timedelta(days=7),
                end_date=datetime.now().date() + timedelta(days=10),
                total_price=Decimal('360.00'),
                status='confirmed'
            )

            # Create a review
            review = Review.objects.create(
                property=property1,
                user=guest,
                rating=5,
                comment='Great place! Very clean and comfortable.'
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully created sample data:')
            )
            self.stdout.write(f'  - 3 users (2 hosts, 1 guest)')
            self.stdout.write(f'  - 3 properties')
            self.stdout.write(f'  - 1 booking')
            self.stdout.write(f'  - 1 review')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating sample data: {e}')
            )