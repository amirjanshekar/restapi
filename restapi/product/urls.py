from .views import ArticleList, ProductList
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'product', ProductList)
router.register(r'article', ArticleList)


urlpatterns = [
    path('', include(router.urls)),
    path('/<int:id>/', include(router.urls)),
]
