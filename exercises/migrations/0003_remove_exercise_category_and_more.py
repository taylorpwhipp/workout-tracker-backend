# Generated by Django 4.2.9 on 2024-02-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_muscle_group_large_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='category',
        ),
        migrations.AlterField(
            model_name='muscle_group',
            name='large_group',
            field=models.CharField(choices=[('legs', 'Legs'), ('shoulders', 'Shoulders'), ('back', 'Back'), ('abs', 'Abs'), ('chest', 'Chest')], default='none', max_length=32),
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.ManyToManyField(to='exercises.category'),
        ),
    ]
