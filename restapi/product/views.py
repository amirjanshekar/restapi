from rest_framework.permissions import IsAuthenticated
from .models import Article, Product
from .serializers import ArticleSerializer, ProductSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework import viewsets
from rest_framework import mixins


class ProductList(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ArticleList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
