# Generated by Django 4.1.3 on 2022-11-28 11:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField()),
                ('allocated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DayMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_num', models.CharField(max_length=20)),
                ('students', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_start', models.TimeField(default='8:30')),
                ('work_end', models.TimeField(default='10:00')),
                ('work_day', models.DateField(default=datetime.date.today)),
                ('work_type', models.CharField(choices=[('Практическое занятие', 'Практическое занятие'), ('Лекции', 'Лекции')], max_length=50)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.classroom')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.subject')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.tutor')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='tutor',
            field=models.ManyToManyField(to='timetable.tutor'),
        ),
    ]
