# Generated by Django 3.0.2 on 2020-06-28 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('event_id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='id')),
                ('event_name', models.CharField(max_length=200, verbose_name='일정')),
                ('location', models.CharField(max_length=200, verbose_name='장소')),
                ('start_date', models.CharField(max_length=50, verbose_name='시작일')),
                ('end_date', models.CharField(max_length=50, verbose_name='종료일')),
                ('all_day', models.BooleanField(verbose_name='종일')),
                ('description', models.TextField(default='', verbose_name='설명')),
                ('updated', models.DateTimeField(default=datetime.datetime(2020, 6, 28, 13, 27, 2, 428808, tzinfo=utc), verbose_name='수정일')),
                ('deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
            ],
            options={
                'verbose_name': '학사일정',
                'verbose_name_plural': '학사일정',
                'db_table': '학사일정',
            },
        ),
    ]
