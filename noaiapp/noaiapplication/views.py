
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

@api_view(['POST','GET'])
def QuestionList(request):
    if request.method=='GET':
        questions=Question.objects.all()
        serializer=QuestionSerializer(questions, many=True)
        return Response(serializer.data,status=200)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors,status=404)
@api_view(['GET','PUT','DELETE'])
def QuestionDetails(request,pk):
    try:
        question=Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=404)
    if request.method=='GET':
        serializer=QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=QuestionSerializer(question,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404)
    elif request.method=='DELETE':
        question.delete()
        return Response(status=204)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def crash_api(request):
    x = 10 / 1
    return Response({"msg": "crash"})

@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
@parser_classes([MultiPartParser, FileUploadParser])
def productdemoList(request):
    if request.method=='GET':
        productsdemolist=ProductDemo.objects.all()
        serializer=ProductdemoSerializer(productsdemolist,many=True)
        return Response(serializer.data,status=201)
    if request.method=='POST':
        serializer=ProductdemoSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)
    
@api_view(['GET','DELETE','PUT'])
@parser_classes([MultiPartParser, FileUploadParser])
def productdemoDetails(request,id,*args,**kwargs):
    print(request.data)
    print(id)
    try:
        productdemo=ProductDemo.objects.get(pk=id)
        print(productdemo)
    except ProductDemo.DoesNotExist:
        return Response(status=404) 
    if request.method=='GET':
        serializer=ProductdemoSerializer(productdemo)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ProductdemoSerializer(productdemo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        productdemo.delete()
        return Response(status=204)

@api_view(['GET','POST'])
def Customerlist(request):
    if request.method=='POST':
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    elif request.method=='GET':
        query_set=Customer.objects.all()
        name=request.query_params.get('name')
        if name is not None:
            query_set=query_set.filter(name=name)
        
        phonenumber=request.query_params.get("phonenumber")
        if phonenumber is not None:
             query_set=query_set.filter(phonenumber=phonenumber)

        address=request.query_params.get('address')
        if address is not None:
            query_set=query_set.filter(address=address)
        serializer=CustomerSerializer(query_set,many=True)
        return Response(serializer.data,status=200)
    
@api_view(['GET','PUT','DELETE'])
def CustomerDetails(request,pk):
    try:
        customer=Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=404)
    if request.method=='GET':
        serializer=CustomerSerializer(customer)
        return Response(serializer.data,status=200)
    elif request.method=='PUT':
        serializer=CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404)
    elif request.method=='DELETE':
        customer.delete()
        return Response(status=205)


        