# Generated by Django 4.1.3 on 2022-11-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_alter_group_group_num_alter_subject_subject_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='allocated',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='place',
            field=models.CharField(max_length=20),
        ),
    ]
