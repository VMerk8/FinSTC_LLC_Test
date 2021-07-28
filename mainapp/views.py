from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Dealer, Car, Manufacturer
from .serializers import DealerSerializer, CarSerializer, ManufacturerSerializer


class DealerView(ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


class CarView(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    """ Запрос выдаёт список автомобилей, которые есть у производителя """

    @action(detail=False, methods=['get'], url_name='get_manufacturer_cars')
    def get_manufacturer_cars(self, request):
        result = Car.objects.filter(manufacturer_id=request.query_params.get('manufacturer_id')).values('car_model')
        return Response(result)

    """ Запрос выдаёт список автомобилей, которые есть у дилера """

    @action(detail=False, methods=['get'], url_name='get_dealer_cars')
    def get_dealer_cars(self, request):
        result = Car.objects.filter(dealer_id=request.query_params.get('dealer_id')).values('car_model')
        return Response(result)


class ManufacturerView(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
