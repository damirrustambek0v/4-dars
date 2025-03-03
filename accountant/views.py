from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils.timezone import now
from .models import Author, Genre, Book, BookCopy, BookLending
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, BookCopySerializer, BookLendingSerializer

# AUTHOR (Mualliflar)
class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'

class AuthorBooksAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs['id']
        return Book.objects.filter(author_id=author_id)


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BooksAPIView(generics.ListAPIView):
    serializer_class = BookCopySerializer

    def get_queryset(self):
        book_id = self.kwargs['id']  #
        return BookCopy.objects.filter(book_id=book_id)


class BookCopyListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class BookCopyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

@api_view(['GET'])
def available_book_copies(request):
    available_copies = BookCopy.objects.filter(is_available=True)
    serializer = BookCopySerializer(available_copies, many=True)
    return Response(serializer.data)


class BookLendingListCreateAPIView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer

class BookLendingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer

@api_view(['PUT'])
def return_book(request, pk):
    try:
        lending = BookLending.objects.get(pk=pk)
        lending.returned = True
        lending.save()
        return Response({"message": "Kitob qaytarildi!"}, status=status.HTTP_200_OK)
    except BookLending.DoesNotExist:
        return Response({"error": "Bunday kitob berilgan emas!"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def overdue_books(request):
    overdue = BookLending.objects.filter(due_date__lt=now(), returned=False)
    serializer = BookLendingSerializer(overdue, many=True)
    return Response(serializer.data)
