from django.db import models


class Dealer(models.Model):
    dealer_name = models.CharField(max_length=100, verbose_name="Имя дилера")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    email = models.EmailField(max_length=100, verbose_name="Email", null=True)

    def __str__(self):
        return self.dealer_name

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100, verbose_name='Имя производителя')

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Car(models.Model):
    car_model = models.CharField(max_length=100, verbose_name="Модель автомобиля")
    release_year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")
    dealer_id = models.ManyToManyField(Dealer, verbose_name="Дилеры")
    manufacturer_id = models.ForeignKey(
        Manufacturer, related_name="cars", verbose_name="Производитель", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
