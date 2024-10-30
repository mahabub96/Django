# from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     birthdate = models.DateField()

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     publication_date = models.DateField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2,null=True)  # Price field added

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)  # Link to Publisher
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        permissions = [
            ("can_view_books", "Can view books"),  # Custom permission
        ]

    def __str__(self):
        return self.title
