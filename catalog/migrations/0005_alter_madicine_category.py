# Generated by Django 4.0.3 on 2022-03-24 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_madicine_category_madicine_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madicine',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='madicines', to='catalog.category'),
        ),
    ]
