# Generated by Django 4.1.3 on 2022-12-01 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0012_delete_worktype'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ('work_type',),
            },
        ),
        migrations.AddField(
            model_name='timetable',
            name='work_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='timetable.worktype'),
            preserve_default=False,
        ),
    ]
