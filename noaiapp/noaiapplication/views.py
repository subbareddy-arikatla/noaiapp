
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,parser_classes
from .serializers import StudentSerializer,QuestionSerializer,ProductSerializer,ProductdemoSerializer,CustomerSerializer,BookSerializer
from .models import Student,Question,Product,ProductDemo,Customer,Book
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from rest_framework import status
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create + List
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# Create + List
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Book created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Retrieve + Update + Delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Book updated successfully",
                "data": serializer.data
            })
        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Book deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

