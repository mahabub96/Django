# books/signals.py
import secrets
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

# Signal to generate a unique hex code before saving the book
@receiver(post_save, sender=Book)
def generate_unique_hex(sender, instance, **kwargs):
    # Generate a unique 8-byte hex code
    unique_hex = secrets.token_hex(8)
    
    # Print the generated hex code (you can remove this print statement in production)
    print(f"Generated Unique Hex Code for Book: {unique_hex}")
