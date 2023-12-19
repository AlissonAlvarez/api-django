from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del usuario pagador', null=False)
    surname = models.CharField(max_length=200, verbose_name='Apellido del pagador', null=False)
    card_number = models.CharField(max_length=16, verbose_name='Número de tarjeta', null=False)
    card_cvv = models.CharField(max_length=3, verbose_name='Código de seguridad de la tarjeta', null=False)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor a pagar', null=False)
    extra_description = models.TextField(blank=True, null=True, verbose_name='Información adicional del pago')
