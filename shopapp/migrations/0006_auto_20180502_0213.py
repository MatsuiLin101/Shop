# Generated by Django 2.0.4 on 2018-05-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_auto_20180502_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='inventory',
        ),
        migrations.AlterField(
            model_name='order',
            name='pay',
            field=models.CharField(choices=[('CARD', 'PayCard'), ('POD', 'PayPOD')], max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (3, 'On the Way'), (4, 'Delivered'), (2, 'Processing')]),
        ),
    ]