# Generated by Django 2.2.14 on 2021-04-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210409_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artic',
            name='images',
        ),
        migrations.AddField(
            model_name='artic',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
