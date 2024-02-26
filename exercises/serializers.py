from rest_framework import serializers
from .models import Exercise, Muscle_Group

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle_Group
        fields = '__all__'