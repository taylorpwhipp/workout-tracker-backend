from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime
import json
from rest_framework.renderers import JSONRenderer

from .models import Workout, WorkoutExercise
from exercises.models import Exercise
from .serializers import WorkoutSerializer

@csrf_exempt
def create_workout(request):
    if request.method == 'POST':
        try:
            data_list = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        workout_ids = []

        # Create a new Workout instance
        workout = Workout.objects.create(date_created=datetime.now())

        for data in data_list:
            try:
                exercise_name = data.get('exercise_name')
                exercise_format = data.get('exercise_format')
                repetition = data.get('exercise_duration')
            except AttributeError:
                return JsonResponse({'error': 'Invalid data format'}, status=400)

            # Create a new Exercise instance or get an existing one
            exercise, created = Exercise.objects.get_or_create(name=exercise_name)

            # Create a new WorkoutExercise instance for each exercise
            workout_exercise = WorkoutExercise.objects.create(
                workout=workout,
                exercise=exercise,
                format=exercise_format,
                repetition=repetition
            )

            workout_ids.append(workout.id)

        return JsonResponse({'success': True, 'workout_ids': workout_ids})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_workouts(request):
    if request.method == 'GET':
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
