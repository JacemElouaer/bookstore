# Generated by Django 3.2.7 on 2021-09-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=8)),
                ('age', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
