# Generated by Django 5.1.2 on 2024-10-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view_books', 'Can view books')]},
        ),
    ]
