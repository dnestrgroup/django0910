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
# simple class to work with GET and POST requests
# the class Response transform data to JSON
class ArticleAPIView(APIView):
    def get(self, request):
        # Simple response
        # return Response({'title': 'House model11'})

        # from DB response
        # 1. Get list of objects
        # 2. Transform it to JSON (via serializer)
        lst = Article.objects.all().values()
        return Response({"posts:": ArticleSerializer(lst, many=True).data})

    def post(self, request):
        # Simple response via POST-request
        # return Response({'title': 'House model22'})

        # This method adds new row to DB
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = ArticleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        # Получаем объект статьи на основе предоставленного первичного ключа
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Метод DELETE не разрешен"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Объект не существует"})

        # Удаляем объект статьи
        instance.delete()

        return Response({"message": "Статья успешно удалена"})


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    from rest_framework import generics


from rest_framework.response import Response
from rest_framework import status


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def delete(self, request, *args, **kwargs):
        # Получите первичный ключ статьи для удаления
        pk = kwargs.get("pk", None)
        if not pk:
            return Response(
                {"error": "Первичный ключ не указан"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Получите объект статьи на основе первичного ключа
            article = Article.objects.get(pk=pk)
            # Удалите объект статьи
            article.delete()
            return Response(
                {"message": "Статья удалена успешно"}, status=status.HTTP_204_NO_CONTENT
            )
        except Article.DoesNotExist:
            return Response(
                {"error": "Статья не найдена"}, status=status.HTTP_404_NOT_FOUND
            )
