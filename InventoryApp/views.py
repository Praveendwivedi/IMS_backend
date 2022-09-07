from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from InventoryApp.models import Factories, Products
from InventoryApp.serializers import FactoriesSerializer, ProductsSerializer

from django.core.files.storage import default_storage

from rest_framework.views import APIView

from rest_framework.response import Response

from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def factoryApi(request,id=0):
    if request.method=='GET':
        if id!=0:
            factory=Factories.objects.get(FactoryId=id)
            factory_serializer=FactoriesSerializer(factory)
            return JsonResponse(factory_serializer.data,safe=False)
        factories = Factories.objects.all()
        factories_serializer=FactoriesSerializer(factories,many=True)
        return JsonResponse(factories_serializer.data,safe=False)
    
    elif request.method=='POST':
        factory_data = JSONParser().parse(request)
        print(factory_data)
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
            factories = Factories.objects.all()
            factories_serializer=FactoriesSerializer(factories,many=True)
            return JsonResponse(factories_serializer.data,safe=False)
            # return JsonResponse("Added successfully",safe=False)
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
        print(products)
        products_serializer=ProductsSerializer(products,many=True)
        # print(products_serializer)
        return JsonResponse(products_serializer.data,safe=False)
    
    elif request.method=='POST':
        form = Products(request.POST,request.FILES)
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

class productClass(APIView):
    def get(self,request,id=0):
        products = Products.objects.select_related().filter(Factory=id)
        # products = Products.objects.all()
        products_serializer=ProductsSerializer(products,many=True)
        # form=FormData()
        return JsonResponse(products_serializer.data,safe=False)
    
    def post(self,request):
        products_serializer=ProductsSerializer(data=request.data)
        print(request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            # products = Products.objects.select_related().filter(Factory=id)
            # products_serializer=ProductsSerializer(products,many=True)
            # print(products_serializer)
            return JsonResponse(products_serializer.data)
        return Response({"status":500})
    def delete(self,request,id=0):
        product=Products.objects.get(ProductId=id)
        product.delete()
        return Response({"status":200})
class productDetail(APIView):
    def get(self,request,id=0):
        product=Products.objects.get(ProductId=id)
        # products = Products.objects.all()
        products_serializer=ProductsSerializer(product)
        print(products_serializer.data)
        return Response(products_serializer.data)
    def put(self,request,id=0):
        product=Products.objects.get(ProductId=request.data['ProductId'])
        print("put",product)
        # products = Products.objects.all()
        products_serializer=ProductsSerializer(product,data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data)
        return Response({"status":500,"message":"error:("})
