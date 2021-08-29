from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return render(JsonResponse(serializer.data, status=201))
        return render(JsonResponse(serializer.errors, status=400))
    
