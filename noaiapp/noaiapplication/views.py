
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import StudentSerializer,QuestionSerializer,ProductSerializer
from .models import Student,Question,Product
from rest_framework.parsers import JSONParser

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
        return Response(serializer.data,)

def student_details(request,pk, *args, **kwargs):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=404)
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    elif request.method=='DELETE':
        student.delete()
        return Response(status=204)
    elif request.method=='PUT':
        data=JSONParser().parser(request)
        serializer=StudentSerializer(student,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
@api_view(['POST','GET'])
def QuestionList(request):
    if request.method=='GET':
        questions=Question.objects.all()
        serializer=QuestionSerializer(questions)
        return Response(serializer.data,status=200)
    elif request.method=='POST':
        data=JSONParser().parser(request)
        serializer=QuestionSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors,status=404)
def QuestionDetails(request,pk):
    try:
        question=Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=404)
    if request.method=='GET':
        serializer=QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method=='PUT':
        data=JSONParser.Parser(request)
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
    serializer = ProductSerializer(products)
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
    x = 10 / 0
    return Response({"msg": "crash"})

@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
