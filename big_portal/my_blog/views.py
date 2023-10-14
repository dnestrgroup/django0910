from django.shortcuts import render

from django.http import HttpResponse
from .models import Article

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