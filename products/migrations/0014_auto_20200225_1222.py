# Generated by Django 3.0.2 on 2020-02-25 12:22

from django.db import migrations, models
import products.media_locations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200225_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=products.media_locations.upload_location_main_image),
        ),
    ]
