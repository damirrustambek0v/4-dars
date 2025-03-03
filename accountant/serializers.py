
from rest_framework import serializers
from .models import Author, Genre, Book, BookCopy, BookLending


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'description', 'page_count', 'language']


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ['id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date']


class BookLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = ['id', 'book_copy', 'borrower_name', 'borrower_email', 'borrower_date', 'due_date', 'returned_date', 'status']
