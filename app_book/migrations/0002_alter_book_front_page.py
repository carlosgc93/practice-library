# Generated by Django 4.2.6 on 2023-10-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='front_page',
            field=models.ImageField(upload_to='front_images'),
        ),
    ]