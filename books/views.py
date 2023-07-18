from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from rest_framework import generics, status
from .serializers import BookSerializer


# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(id=3)
        return queryset
        # data = {
        #     'data': queryset
        # }
        # return Response(data)

class BookViewApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serialized_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(books)} books',
            'books': serialized_data
        }
        return Response(data)

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serialized_data = BookSerializer(data=data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(data)
        raise ValidationError(serialized_data.errors)



class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.filter(id=pk)
            serializer_data = BookSerializer(book[0]).data

            data = {
                'status': 'succesful',
                'book': serializer_data

            }
            return Response(data)
        except Exception:
            return Response(
                {'status': 'Doesnt exist'}, status=status.HTTP_404_NOT_FOUND
            )
class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        data = request.data
        serialized_data = BookSerializer(instance=book, data=data, partial=True)
        if serialized_data.is_valid(raise_exception=True):
            book_saved = serialized_data.save()
            return Response(
                {'status': 'succesfully saved'},
                status=status.HTTP_200_OK
            )
class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = get_object_or_404(Book, id=pk)
            book.delete()
            return Response(
                {'stratus': True,
                 'message': 'Succesfully'},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {'status': False,
                 'message': 'No deleted'},
                status=status.HTTP_400_BAD_REQUEST
            )


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# function based view in DRF
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
class BookUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def book_list(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
