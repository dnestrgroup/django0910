from rest_framework import serializers
from .models import Article

# Serializer that work with tables
# We take all fields from Article
# and turn them to JSON
# and send it to the client
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    photo = serializers.CharField()