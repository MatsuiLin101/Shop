# Generated by Django 2.0.4 on 2018-05-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay',
            field=models.CharField(choices=[('CARD', 'PayCard'), ('POD', 'PayPOD')], max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(4, 'Delivered'), (3, 'On the Way'), (1, 'Pending'), (2, 'Processing')]),
        ),
    ]
