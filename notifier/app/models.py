from django.db import models

# Create your models here.


class BitcoinPrice(models.Model):
    price = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Bitcoin USD Price'
        verbose_name_plural = 'Bitcoin USD Prices'


class BitcoinBRPrice(models.Model):
    price = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Bitcoin BRL Price'
        verbose_name_plural = 'Bitcoin BRL Prices'
