from django.contrib import admin
from .models import Profile
from accounts.models import FavFoodList

# Register your models here.
admin.site.register(Profile)
admin.site.register(FavFoodList)