# Generated by Django 3.0.5 on 2022-12-11 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0007_image_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]