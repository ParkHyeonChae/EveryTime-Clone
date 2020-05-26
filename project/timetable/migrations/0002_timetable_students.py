# Generated by Django 3.0.2 on 2020-05-26 05:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name='수강학생'),
        ),
    ]
