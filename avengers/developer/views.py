from django.shortcuts import render
from .serialzers  import  DeveloperSerializers
from .models import  Developer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# Create your views here.
class  MyView(APIView):
    
    
    def get(self,request,pk=None,format=None):
        # if pk is not None:
        #         stu = Developer.objects.get(id=pk)
        #         serializers = DeveloperSerializers(stu)
        #         return Response(serializers.data,status=status.HTTP_200_OK)
           
        # stu =Developer.objects.all()
        # serializers = DeveloperSerializers(stu,many=True)
        # return Response(serializers.data,status=status.HTTP_200_OK)
        
        return render(Http)
        
    def post(self,request,format=None):
        serializers = DeveloperSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            res  ={"msg":'data is inserted'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def  patch(self,request,pk,format=None):
        stu =Developer.objects.get(id=pk)
        serializers =DeveloperSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'data updata successfully'}
            return Response(res, status=status.HTTP_202_ACCEPTED)
        
        
    def delete(self,request,pk,format=None):
        stu = Developer.objects.get(id=pk)
        stu.delete()
        res ={'msg':'data deleted successfully'}
        return Response(res,status=status.HTTP_200_OK)