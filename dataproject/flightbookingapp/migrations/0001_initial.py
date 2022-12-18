# Generated by Django 3.1.1 on 2022-12-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flightbooking',
            fields=[
                ('Cust_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Cust_Name', models.CharField(max_length=100)),
                ('Cust_Age', models.IntegerField()),
                ('Cust_Email', models.EmailField(max_length=254)),
                ('Cust_Gender', models.CharField(max_length=100)),
            ],
        ),
    ]