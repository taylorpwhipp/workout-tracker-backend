from django.contrib import admin
from .models import Workout, WorkoutExercise

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [WorkoutExerciseInline]

admin.site.register(Workout, WorkoutAdmin)
# admin.site.register(WorkoutExercise)