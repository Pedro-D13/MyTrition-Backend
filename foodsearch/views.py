# Django imports
from django.shortcuts import render, get_object_or_404
from foodsearch.models import FoodCategory,FoodDescription, FoodNutrient,Nutrient,BrandedFoodCategory
from foodsearch.serializers import (
        FoodCategorySerializer,FoodDescriptionSerializer,FoodNutrientSerializer,BrandedFoodCategorySerializer,NutrientSerializer,NutritionConverter)
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse, Http404

# DRF imports
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler

class ListCategoryVS(viewsets.ViewSet):
    # List all the food categories to choose from before making a search
    def list(self,request):
        # See if you can cache this query you don't need to keep hitting the database to get just the same categories
        qs = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        queryset = FoodCategory.objects.all()
        category = get_object_or_404(queryset,pk=pk)
        serializer = FoodCategorySerializer(category)
        return Response(serializer.data)
    

# class FoodDescriptionVS(viewsets.ViewSet):
#     ''' 
#     ids for Protein,
#     Total lipid (fat),
#     Carbohydrate, by difference,
#     Energy,
#     Sugars totalincluding NLEA
#     '''
#     ids = [2000,1003,1004,1008,1005]


#     def list(self,request,cat_id,desc):
#         foodDescQS = FoodDescription.objects.filter(food_category_id=cat_id , description__search=desc)
#         serializer = FoodDescriptionSerializer(foodDescQS,many=True)
#         return Response(serializer.data[:50])


#     def retrieve(self,request,**kwags):
#         final_result = NutritionConverter(self)
#         return Response(final_result)

class BrandedFoodListVS(viewsets.ViewSet):
    # list all the categoriess
    def listCat(self,request,desc):
        branded = FoodDescription.objects.filter(description__search=desc).prefetch_related('brandedfoodcategory').values('fdc_id').exclude(brandedfoodcategory__branded_food_category__isnull=True)
        brandedFoods= BrandedFoodCategory.objects.filter(fdc_id__in=branded)
        brandedFoodsCats=brandedFoods.distinct('branded_food_category')
        serializer = BrandedFoodCategorySerializer(brandedFoodsCats, many=True)
        if len(serializer.data) is 0:
            return Response(data="Not found",status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def listGenCat(self,request,desc):
        generic = FoodDescription.objects.filter(description__search=desc).prefetch_related('foodcategory').values('food_category_id').order_by()
        genericFoodsCats=FoodCategory.objects.filter(id__in=generic)
        serializer2 = FoodCategorySerializer(genericFoodsCats, many= True)


    def listItemsFromCat(self,request,desc,cat):
        final_result=FoodDescription.objects.filter(description__search=desc,brandedfoodcategory__branded_food_category__search=cat).prefetch_related('brandedfoodcategory').values('description','fdc_id').order_by()
        serializer = FoodDescriptionSerializer(final_result,many=True)
        return Response(serializer.data)

class NutrientDataVS(viewsets.ViewSet):
    ids = [2000,1003,1004,1008,1005]
    def retrieve(self,request,**kwags):
        final_result = NutritionConverter(self,request)
        return Response(final_result)
