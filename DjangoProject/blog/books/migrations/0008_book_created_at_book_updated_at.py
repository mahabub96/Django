# Generated by Django 5.1.2 on 2024-10-30 10:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
