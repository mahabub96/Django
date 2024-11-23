from django.urls import path
from . import views
from .views import AuthorListCreateAPIView, PublisherListCreateAPIView, BookListCreateAPIView, BookGetUpdateDelete, create_book
from books.views import my_view, BookListView, MyView, ContactFormView, BookApiListView
from django.shortcuts import render

urlpatterns = [
    path('initial/',my_view),
    path('initial_class/', MyView.as_view()),
    path('list/', BookListView.as_view(), name='book_list'),
   ## path('books/', views.book_list, name='book_list'),
    path('contact/add', ContactFormView.as_view()),
    path('create-book/', create_book, name='create-book'),
    path('books_rest/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('publishers/', PublisherListCreateAPIView.as_view(), name='publisher-list-create'),
    path('contact_success/', lambda request: render(request, 'success/contact_success.html'), name='contact_success'),
    path('books_up/<int:pk>/', BookGetUpdateDelete.as_view(), name='book-detail'),
    path('Api_list/', BookApiListView.as_view()),
    
]