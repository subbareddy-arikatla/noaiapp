
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import StudentSerializer,QuestionSerializer
from .models import Student,Question
@api_view(['GET','POST',])
def student_list(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=StudentSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    elif request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data, safe=False)

def student_details(request,pk):
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