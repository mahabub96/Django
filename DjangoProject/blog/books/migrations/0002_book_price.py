# Generated by Django 5.1.2 on 2024-10-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null='true'),
            preserve_default='true',
        ),
    ]
