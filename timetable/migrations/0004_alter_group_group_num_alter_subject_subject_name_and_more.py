# Generated by Django 4.1.3 on 2022-11-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_rename_name_subject_subject_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_num',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='work_end',
            field=models.TimeField(default='09:50'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='work_start',
            field=models.TimeField(default='8:20'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='work_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tutor_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
