from django.contrib import admin
from .models import Exercise, Category, Muscle_Group

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Category)
admin.site.register(Muscle_Group)