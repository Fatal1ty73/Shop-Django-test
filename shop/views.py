from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shop.models import *
from shop.serializers import *


@csrf_exempt
def store_list(request):
    """
    List all code store, or create a new store.
    """
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def store_detail(request, pk):
    """
    Retrieve, update or delete a code store.
    """
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(store, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        store.delete()
        return HttpResponse(status=204)