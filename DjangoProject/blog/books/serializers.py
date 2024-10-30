# book/serializers.py
from django.utils import timezone
from rest_framework import serializers
from .models import Book, Author, Publisher
from datetime import date, timedelta


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        title = attrs.get('title')
        description = attrs.get('description')
        publication_date = attrs.get('publication_date')
        price = attrs.get('price')
        
        # Title length validation
        if title and len(title) > 100:
            raise serializers.ValidationError("Title must be under 100 characters.")
        
        # Description word count validation
        if description and len(description.split()) < 10:
            raise serializers.ValidationError("Description must contain at least 10 words.")
        
        # Publication date validation
        one_month_ago = date.today() - timedelta(days=30)
        if publication_date and publication_date > one_month_ago:
            raise serializers.ValidationError("Publication date must be at least one month old.")
        
        # Price range validation
        if price is not None and (price < 100 or price > 10000):
            raise serializers.ValidationError("Price must be between 100 and 10,000.")
        
        return attrs
    
    def create(self, validated_data):
        author = validated_data.pop('author')
        author_serializer = AuthorSerializer(data=author)
        if author_serializer.is_valid():
            author_instance = author_serializer.save()
            validated_data['author']= author_instance
        
        publisher = validated_data.pop('publisher')  # Pop publisher data from validated_data
        publisher_serializer = PublisherSerializer(data=publisher)  # Create a Publisher serializer instance

        if publisher_serializer.is_valid():  # Validate the Publisher data
            publisher_instance = publisher_serializer.save()  # Save the Publisher instance
            validated_data['publisher'] = publisher_instance  # Assign the Publisher instance to validated_data
            
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data  ['updated_at'] = timezone.now()
        return super().update(instance, validated_data)