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

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()