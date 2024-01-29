import datetime
from django.db import models


class PaymentData(models.Model):
    # Address data
    city = models.CharField(max_length=20, verbose_name='Город')
    full_address = models.CharField(max_length=90, verbose_name='Полный адрес')
    post_index = models.CharField(max_length=5, verbose_name='Почтовый индекс')
    country = models.CharField(max_length=30, verbose_name='Страна')

    # Card data
    card_number = models.CharField(max_length=19, verbose_name='Номер карты')
    expiry_date = models.CharField(max_length=5, verbose_name='Дата истечения срока')
    cvv = models.CharField(max_length=3, verbose_name='CVV')
    cardholder_name = models.CharField(max_length=25, verbose_name='Имя на карте')

    time_payment = models.DateTimeField(verbose_name='Дата и время оплаты', default=datetime.datetime.now())
    cart = models.JSONField(null=True, verbose_name='Товары')
    total_price = models.IntegerField(verbose_name='Итоговая цена', null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.country}, {self.city}, {self.post_index}, Дата: {self.time_payment}'
