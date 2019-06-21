# Generated by Django 2.0 on 2019-06-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Temperature in celcius')),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Humidity in percentage')),
                ('gas', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Gas in pressure')),
            ],
        ),
    ]