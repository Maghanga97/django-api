# Generated by Django 4.1.1 on 2022-11-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_no', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=100)),
                ('owns_car', models.BooleanField()),
                ('owns_realty', models.BooleanField()),
            ],
        ),
    ]
