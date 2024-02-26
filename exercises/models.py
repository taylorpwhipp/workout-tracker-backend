from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    # this is the type of workout- like HIIT, strenth, pilates, etc

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Muscle_Group(models.Model):
    LEGS = 'legs'
    ARMS = 'arms',
    SHOULDERS = 'shoulders'
    BACK = 'back'
    ABS ='abs'
    CHEST ='chest'

    LARGE_GROUPS = [
        (LEGS, _('Legs')),
        (SHOULDERS, _('Shoulders')),
        (BACK, _('Back')),
        (ABS, _('Abs')),
        (CHEST,_('Chest')),
    ]

    name= models.CharField(max_length=255)
    large_group = models.CharField(max_length=32,choices=LARGE_GROUPS,default ='none')

    class Meta:
        verbose_name_plural = "Muscle Groups"

    def __str__(self):
        return f"{self.name}"


class Exercise (models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    requires_weght = models.BooleanField()
    low_impact = models.BooleanField()
    is_compound_movement = models.BooleanField()
    muscle_group = models.ManyToManyField(Muscle_Group)

    def __str__(self):
      return f"{self.name}"




