from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artical
from .serializers import ArticalSerializer
from django.template.defaultfilters import date
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def article_list(request):

    if request.method == 'GET':
        articles = Artical.objects.all()
        serializer = ArticalSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe = False)
         
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)   
@csrf_exempt
def artical_detail(request, pk):
    try:
        article = Artical.objects.get(pk=pk)
    
    except Artical.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ArticalSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(data=data)
        if serializer.is_valid():
            serializer.save();
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)    