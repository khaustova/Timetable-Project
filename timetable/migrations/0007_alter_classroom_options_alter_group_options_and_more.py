# Generated by Django 4.1.3 on 2022-11-29 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_remove_classroom_allocated_alter_classroom_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ('place',)},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('group_num',)},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('subject_name',)},
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ('work_day',)},
        ),
        migrations.AlterModelOptions(
            name='tutor',
            options={'ordering': ('tutor_name',)},
        ),
    ]
