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
    #return HttpResponse('<h1>Home Page</h1>')
    # I variant
    # posts = Article.objects.all()
    # res = '<h1> Articles list: </h1>'
    # for item in posts:
    #     res += f'<div><h3>{item.title}</h3> <div>{item.content}</div> </div>'
    # return HttpResponse(res)

    # II variant
    # posts = Article.objects.all()
    posts = Article.objects.order_by('-created_at')
    return render(request, 'my_blog/home.html', {'posts': posts})

def test_page(request):
    return HttpResponse('<h1>Test Page</h1>')



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
        lst = Article.objects.all().values()
        return Response({'posts:': list(lst)})
    
    def post(self, request):
        # Simple response via POST-request
        # return Response({'title': 'House model22'})
        
        # This method adds new row to DB
        post_new = Article.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            photo=request.data['photo'],
        )
        return Response({'post': model_to_dict(post_new)})