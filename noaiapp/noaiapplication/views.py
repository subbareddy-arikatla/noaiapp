
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


from rest_framework import generics
from .models import Student, Professional
from .serializers import StudentSerializer, ProfessionalSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessionalListCreateView(generics.ListCreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book.delete()
        return Response(
            {"message": "Book deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
        
@api_view(['GET','POST',])
def student_list(request, *args, **kwargs):
    if request.method=='POST':
        data=JSONParser().parse(request)
        print(data)
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    elif request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def student_details(request,pk, *args, **kwargs):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=404)
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data, many=True)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=204)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=StudentSerializer(student,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['POST'])
def bulkStudentCreate(request):
    if request.method=='POST':
        students=request.data
        print(students)
        results ={'success':[],'errors':[]}
        if len(students)==0:
            return Response({'error':'empty student'},status=400)
        if not isinstance(students,list):
            return Response({'error':'must be array only'},status=400)
        for student_data in students:
            serializer=StudentSerializer(data=student_data)
            if serializer.is_valid():
                serializer.save()
                results ['success'].append(serializer.data)
            else:
                results['errors'].append({
                    'data':student_data,
                    'errors':serializer.errors
                })
        return Response(results,status=201)

