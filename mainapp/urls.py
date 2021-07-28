from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CarView, ManufacturerView, DealerView

router = DefaultRouter()
router.register('dealer', DealerView, basename='dealer')
router.register('car', CarView, basename='car')
router.register('manufacturer', ManufacturerView)

urlpatterns = [
    path('api/', include(router.urls))
]
