# Generated by Django 2.2.14 on 2021-04-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_artic_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artic',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]