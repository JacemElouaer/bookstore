# Generated by Django 3.2.7 on 2021-09-29 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('Classics', 'Classics'), ('Comic Book or Graphic Novel', 'Comic Book or Graphic Novel'), ('Fantasy', 'Fantasy'), ('Historical Fiction', 'Historical Fiction'), ('Horror', 'Horror'), ('Literary Fiction', 'Literary Fiction')], max_length=200, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('Delivered', 'Delivered'), ('Out of order', 'Out of order'), ('In progress', 'In progress')], max_length=200)),
            ],
        ),
    ]