from rest_framework import serializers
from .models import Article, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'url', 'name', 'family']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'url', 'title', 'author_name', 'description']
