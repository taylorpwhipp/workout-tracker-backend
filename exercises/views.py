from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.core import serializers
from rest_framework.renderers import JSONRenderer
from .models import Exercise, Muscle_Group
from .serializers import ExerciseSerializer, MuscleSerializer

# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Exercise
#         fields = '__all__'


def exercises(request):
    muscle_group_param = request.GET.get('muscle_group', None)

    if muscle_group_param:
        # exercises = Exercise.objects.filter(muscle_group__name=muscle_group_param)
                # Use double-underscore notation to filter by related model's attribute
        exercises = Exercise.objects.filter(muscle_group__large_group=muscle_group_param)
    else:
        exercises = Exercise.objects.all()

    serializer = ExerciseSerializer(exercises, many=True)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json)

def get_muscle_groups(request):

    muscle_groups= Muscle_Group.objects.all()
    print(muscle_groups)
    serializer = MuscleSerializer(muscle_groups, many=True)
    print("Serialized Data:", serializer.data)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json)


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)