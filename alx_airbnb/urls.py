from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import routers
from properties.views import PropertyViewSet
from bookings.views import BookingViewSet
from payments.views import PaymentViewSet
from reviews.views import ReviewViewSet

def api_root(request):
    return JsonResponse({
        'message': 'AirBnB Clone API',
        'endpoints': {
            'admin': '/admin/',
            'api_root': '/api/',
            'properties': '/api/properties/',
            'bookings': '/api/bookings/',
            'payments': '/api/payments/',
            'reviews': '/api/reviews/',
        },
        'status': 'All APIs are running successfully!'
    })

# Router for REST API
router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]