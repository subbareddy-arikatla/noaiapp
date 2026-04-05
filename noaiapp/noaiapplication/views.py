
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class HealthCheck(APIView):
    def get(self,request ,format=None, *args,**kwargs):
        return Response({'status:okay'})

@api_view()
def hello_world(request):
    return Response({'message':'hello world'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method=='POST':
        return Response({'message':'got some data!','data':request.data})
    return Response({'message':'hello world'})