# Generated by Django 5.0 on 2023-12-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del usuario pagador')),
                ('surname', models.CharField(max_length=200, verbose_name='Apellido del pagador')),
                ('card_number', models.CharField(max_length=16, verbose_name='Número de tarjeta')),
                ('card_cvv', models.CharField(max_length=3, verbose_name='Código de seguridad de la tarjeta')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor a pagar')),
                ('extra_description', models.TextField(blank=True, null=True, verbose_name='Información adicional del pago')),
            ],
        ),
    ]
