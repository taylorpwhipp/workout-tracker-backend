from django.db import models
from exercises.models import Exercise

class Workout(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return f"{'{:%B %d, %Y}'.format(self.date_created)}"

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    format = models.CharField(max_length=255)
    repetition = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.workout} - {self.exercise} - {self.format} - {self.repetition}"
