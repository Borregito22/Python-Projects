# Generated by Django 4.0.2 on 2022-02-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('CourseNumber', models.IntegerField()),
                ('InstructorName', models.CharField(default='', max_length=30)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]
