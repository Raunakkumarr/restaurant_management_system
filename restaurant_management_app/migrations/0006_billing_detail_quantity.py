# Generated by Django 4.0.5 on 2022-07-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_management_app', '0005_billing_detail_discount_billing_detail_final_bill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing_detail',
            name='quantity',
            field=models.CharField(default=0, max_length=250, verbose_name='Quantity:'),
            preserve_default=False,
        ),
    ]
