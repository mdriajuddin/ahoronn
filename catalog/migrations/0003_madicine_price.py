# Generated by Django 4.0.3 on 2022-03-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_madicine_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='madicine',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]