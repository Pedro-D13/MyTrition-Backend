# Django imports
from django.shortcuts import render, get_object_or_404
from foodsearch.models import FoodCategory,FoodDescription, FoodNutrient,Nutrient,BrandedFoodCategory
from foodsearch.serializers import (
        FoodCategorySerializer,FoodDescriptionSerializer,FoodNutrientSerializer,BrandedFoodCategorySerializer,NutrientSerializer)
from django.contrib.postgres.search import SearchVector


# DRF imports
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

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
    

class FoodDescriptionVS(viewsets.ViewSet):
    ''' 
    ids for Protein,
    Total lipid (fat),
    Carbohydrate, by difference,
    Energy,
    Sugars totalincluding NLEA
    '''
    ids = [2000,1003,1004,1008,1005]


    def list(self,request,cat_id,desc):
        foodDescQS = FoodDescription.objects.filter(food_category_id=cat_id , description__search=desc)
        serializer = FoodDescriptionSerializer(foodDescQS,many=True)
        return Response(serializer.data[:50])

    def retrieve(self,request,**kwags):
        nutr = FoodNutrient.objects.filter(fdc_id=self.kwargs['fdc_id_arg'] , nutrient_id__in=self.ids)
        nutr_serializer = FoodNutrientSerializer(nutr, many=True)
        result = map(lambda each_nutr: Nutrient.objects.get(id=each_nutr.nutrient_id), nutr)
        serializer = NutrientSerializer(result, many=True)
        zipped_result = zip(serializer.data , nutr_serializer.data)
        final_result = [ dict(**k1, **k2) for (k1,k2) in zipped_result]
        return Response(final_result[:50])


class BrandedFoodListVS(viewsets.ViewSet):
    # list all the categories
    def listCat(self,request, desc):
        qs = FoodDescription.objects.filter(description__search=desc).exclude(
            brandedfoodcategory__branded_food_category__isnull=True
        )
        brandedFoods= BrandedFoodCategory.objects.filter(fdc_id__in=qs)
        brandedFoodsCats=brandedFoods.distinct('branded_food_category')
        serializer = BrandedFoodCategorySerializer(brandedFoodsCats, many=True)
        return Response(serializer.data)

    def listItemsFromCat(self,request,desc,cat):
        final_result=FoodDescription.objects.filter(description__search=desc,brandedfoodcategory__branded_food_category__search=cat)
        serializer = FoodDescriptionSerializer(final_result,many=True)
        return Response(serializer.data)

class NutrientDataVS(viewsets.ViewSet):
    ids = [2000,1003,1004,1008,1005]
    def retrieve(self,request,**kwags):
        nutr = FoodNutrient.objects.filter(fdc_id=self.kwargs['fdc_id_arg'] , nutrient_id__in=self.ids)
        nutr_serializer = FoodNutrientSerializer(nutr, many=True)
        result = map(lambda each_nutr: Nutrient.objects.get(id=each_nutr.nutrient_id), nutr)
        serializer = NutrientSerializer(result, many=True)
        zipped_result = zip(serializer.data , nutr_serializer.data)
        final_result = [ dict(**k1, **k2) for (k1,k2) in zipped_result]
        return Response(final_result)

    def retrieve(self,request,**kwags):
        nutr = FoodNutrient.objects.filter(fdc_id=self.kwargs['fdc_id_arg'] , nutrient_id__in=self.ids)
        nutr_serializer = FoodNutrientSerializer(nutr, many=True)
        result = map(lambda each_nutr: Nutrient.objects.get(id=each_nutr.nutrient_id), nutr)
        serializer = NutrientSerializer(result, many=True)
        zipped_result = zip(serializer.data , nutr_serializer.data)
        final_result = [ dict(**k1, **k2) for (k1,k2) in zipped_result]
        return Response(final_result)



    # branded = BrandedFoodCategory.objects.filter()
    # unbranded = FoodDescription.objects.filter()
    # milk = FoodDescription.objects.filter(description__search="milk").exclude(brandedfoodcategory__branded_food_category__isnull=True)
    # milk_snacks=FoodDescription.objects.filter(description__search="milk", brandedfoodcategory__branded_food_category="Snacks")