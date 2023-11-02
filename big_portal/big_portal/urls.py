"""big_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from my_blog.views import ArticleAPIView
from my_blog.views import ArticleAPIList
from my_blog.views import ArticleAPIUpdate


from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/articleslist/', ArticleAPIView.as_view()),
#     path('api/v1/articleslist/<int:pk>/', ArticleAPIView.as_view()),
#     path('api/v1/articleslist/delete/<int:pk>/', ArticleAPIView.as_view()),
#     path('', include('my_blog.urls'))
# ]

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/articleslist/", ArticleAPIList.as_view()),
    path("api/v1/articleslist/<int:pk>/", ArticleAPIUpdate.as_view()),
    path("api/v1/articleslist/delete/<int:pk>/", ArticleAPIList.as_view()),
    path("", include("my_blog.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
