# Generated by Django 2.0.4 on 2018-05-01 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(max_length=14)),
                ('order_name', models.CharField(max_length=20)),
                ('order_tel', models.PositiveIntegerField()),
                ('order_address', models.CharField(max_length=100)),
                ('pay', models.CharField(choices=[(1, 'PayCard'), (2, 'PayPOD')], max_length=10)),
                ('status', models.IntegerField(choices=[(3, 'On the Way'), (2, 'Processing'), (1, 'Pending'), (4, 'Delivered')])),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
