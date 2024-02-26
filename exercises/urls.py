from django.urls import path
from . import views

urlpatterns = [
    path("", views.exercises, name='exercises'),
    # path("muscle_groups/",views.get_muscle_groups, name ='muscle_groups')
]
