# Generated by Django 3.0.4 on 2020-03-10 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name of Test')),
                ('subs', models.ManyToManyField(to='quizapp.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_description', models.TextField()),
                ('question_number', models.CharField(max_length=2)),
                ('choice_1', models.TextField()),
                ('choice_2', models.TextField()),
                ('choice_3', models.TextField()),
                ('choice_4', models.TextField()),
                ('correct_choice', models.CharField(choices=[('choice_1', 'A'), ('choice_2', 'B'), ('choice_3', 'C'), ('choice_4', 'D')], max_length=10)),
                ('tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Tests')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=3)),
                ('col_name', models.CharField(choices=[('D.J Sanghvi', 'D.J Sanghvi'), ('IIT Powai', 'IIT Powai'), ('IIIT Delhi', 'IIIT Delhi'), ('VJTI', 'VJTI')], max_length=20, verbose_name='College Name:')),
                ('birth_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
