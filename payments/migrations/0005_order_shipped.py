# Generated by Django 5.0.7 on 2024-08-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]