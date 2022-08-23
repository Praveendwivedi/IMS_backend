from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from InventoryApp.models import Factories, Products
from InventoryApp.serializers import FactoriesSerializer, ProductsSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def factoryApi(request,id=0):
    if request.method=='GET':
        factories = Factories.objects.all()
        factories_serializer=FactoriesSerializer(factories,many=True)
        return JsonResponse(factories_serializer.data,safe=False)
    
    elif request.method=='POST':
        factory_data = JSONParser().parse(request)
        factories_serializer=FactoriesSerializer(data=factory_data)
        if factories_serializer.is_valid():
            factories_serializer.save()
            factories = Factories.objects.all()
            factories_serializer=FactoriesSerializer(factories,many=True)
            return JsonResponse(factories_serializer.data,safe=False)
            # return JsonResponse(factories_serializer,safe=False)
        return JsonResponse("Failed to add",safe=False)
    
    elif request.method=='PUT':
        factory_data = JSONParser().parse(request)
        factory=Factories.objects.get(FactoryId=factory_data['FactoryId'])
        factories_serializer=FactoriesSerializer(factory,data=factory_data)
        if factories_serializer.is_valid():
            factories_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    
    elif request.method=='DELETE':
        factory=Factories.objects.get(FactoryId=id)
        factory.delete()
        factories = Factories.objects.all()
        factories_serializer=FactoriesSerializer(factories,many=True)
        return JsonResponse(factories_serializer.data,safe=False)
        # return JsonResponse("Deleted successfully",safe=False)

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        products = Products.objects.select_related().filter(Factory=id)
        products_serializer=ProductsSerializer(products,many=True)
        print(products_serializer)
        return JsonResponse(products_serializer.data,safe=False)
    
    elif request.method=='POST':
        form = FileForm(request.POST,request.FILES)
        # product_data=dir(request)
        product_data=request.POST
        # product_data = JSONParser().parse(request)
        print("pdata:",form)
        # products_serializer=ProductsSerializer(data=product_data)
        # print(products_serializer)
        # if products_serializer.is_valid():
        #     products_serializer.save()
        #     products = Products.objects.select_related().filter(Factory=id)
        #     products_serializer=ProductsSerializer(products,many=True)
        #     print(products_serializer)
        #     return JsonResponse(products_serializer.data,safe=False)
        return JsonResponse("Failed to add",safe=False)
    
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product=Products.objects.get(productId=product_data['productId'])
        products_serializer=ProductsSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    
    elif request.method=='DELETE':
        product=Products.objects.get(ProductId=id)
        product.delete()
        products = Products.objects.select_related().filter(Factory=id)
        products_serializer=ProductsSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)

@csrf_exempt
def SaveFile(request):
    print("req:",request.FILES)
    file_=request.FILES['file']
    file_name=default_storage.save(file_.name,file_)
    return JsonResponse(file_name,safe=False)
