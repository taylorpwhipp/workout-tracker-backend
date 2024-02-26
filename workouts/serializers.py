# from rest_framework import serializers
# from .models import Workout, WorkoutExercise



# class WorkoutSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = Workout
#         fields = '__all__'

from rest_framework import serializers
from .models import Workout, WorkoutExercise

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ('exercise_name', 'format', 'repetition')

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ('id', 'date_created', 'exercises')

    def get_exercises(self, obj):
        workout_exercises = WorkoutExercise.objects.filter(workout=obj)
        exercise_serializer = WorkoutExerciseSerializer(workout_exercises, many=True)
        return exercise_serializer.data


