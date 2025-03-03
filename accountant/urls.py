from django.urls import path
from .views import (AuthorListCreateAPIView, AuthorDetailAPIView,
                    AuthorBooksAPIView, GenreListCreateAPIView, BookListCreateAPIView, BookDetailAPIView,
                    BooksAPIView, BookCopyListCreateAPIView, BookCopyDetailAPIView, available_book_copies,
                    BookLendingListCreateAPIView, BookLendingDetailAPIView, return_book, overdue_books
                    )

urlpatterns = [
    # Author URLs
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('authors/<int:id>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('authors/<int:id>/books/', AuthorBooksAPIView.as_view(), name='author-books'),

    # Genre URLs
    path('genre/', GenreListCreateAPIView.as_view(), name='genre-list'),

    # Book URLs
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:id>/copies/', BooksAPIView.as_view(), name='book-copies'),

    # Book Copy URLs
    path('copies/', BookCopyListCreateAPIView.as_view(), name='bookcopy-list'),
    path('copies/<int:pk>/', BookCopyDetailAPIView.as_view(), name='bookcopy-detail'),
    path('copies/available/', available_book_copies, name='available-book-copies'),

    # Lending URLs
    path('lendings/', BookLendingListCreateAPIView.as_view(), name='booklending-list'),
    path('lendings/<int:pk>/', BookLendingDetailAPIView.as_view(), name='booklending-detail'),
    path('lendings/<int:pk>/return/', return_book, name='return-book'),
    path('lendings/overdue/', overdue_books, name='overdue-books'),
]
