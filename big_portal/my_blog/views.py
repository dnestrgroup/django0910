from django.shortcuts import render
from django.forms import model_to_dict

# Libraries for simple page render
from django.http import HttpResponse
from .models import Article

# Libraries for REST-framework (work with generics)
from rest_framework import generics
from .serializers import ArticleSerializer

# Libraries for REST-framework (work with APIView, get, post)
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status


# Create your views here.
def home(request):
    # return HttpResponse('<h1>Home Page</h1>')
    # I variant
    # posts = Article.objects.all()
    # res = '<h1> Articles list: </h1>'
    # for item in posts:
    #     res += f'<div><h3>{item.title}</h3> <div>{item.content}</div> </div>'
    # return HttpResponse(res)

    # II variant
    # posts = Article.objects.all()
    posts = Article.objects.order_by("-created_at")
    return render(request, "my_blog/home.html", {"posts": posts})


def test_page(request):
    return HttpResponse("<h1>Test Page</h1>")


# The 1-st view for REST-framework
# in generics module we have classes to work with REST-framework
# class ArticleAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# The 2-nd view for REST-framework
# simple class to work with requests
# Here we will realize GET, POST, PUT, DELETE
# the class Response transform data to JSON
# class ArticleAPIView(APIView):
#     def get(self, request):
#         lst = Article.objects.all().values()
#         return Response({"posts:": ArticleSerializer(lst, many=True).data})

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})

#         serializer = ArticleSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         # Получаем объект статьи на основе предоставленного первичного ключа
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Метод DELETE не разрешен"})

#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({"error": "Объект не существует"})

#         instance.delete()
#         return Response({"message": "Статья успешно удалена"})


# The 3-rd view for REST-framework
# 1) ListCreateAPIView - supports GET and POST
# 2) UpdateAPIView - supports PUT
# 3) RetrieveUpdateDestroyAPIView - supports GET, PUT, DELETE
class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleAPIUpdate(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
