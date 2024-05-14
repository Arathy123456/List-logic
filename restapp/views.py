from urllib import request

from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import blog
from .serializer import  blogSerializer

from rest_framework.views import APIView


def todo_list(request):
    todos=blog.objects.all()
    return render(request,'todo.html',{'todos':todos})
class ListblogAPIView(APIView):
    def get(self,request):
        datas = blog.objects.all()
        serializer = blogSerializer(datas, many=True)
        return Response(serializer.data)
        return redirect('todo_list')
class blogDetailAPIView(APIView):
    def get(self,request,pk):
        todos = blog.objects.get(id=pk)
        serializer = blogSerializer(todos, many=False)
        return Response(serializer.data)
class CreateblogAPIView(APIView):
     def post(self,request):
        serializer = blogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class UpdateblogAPIView(APIView):
    def post(self,request,pk,title,description):
        data = blog.objects.get(id=pk)
        serializer = blogSerializer(instance=data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class deleteblogAPIView(APIView):
    def get(self,request,pk):
        data=blog.objects.get(id=pk)
        data_instance=blog.objects.get(id=pk)
        data_instance.delete()
        return Response("DELETED")
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todos=blog(title=title, description=description)
        todos.save()
        return redirect('todo_list')
    return render(request,'todo.html')


