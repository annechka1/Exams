# Generated by Django 3.1.4 on 2020-12-21 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_class', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_of_exams', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marks_exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.IntegerField(default=0)),
                ('english', models.IntegerField(default=0)),
                ('russian', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname_of_teacher', models.CharField(max_length=100)),
            ],
        ),
    ]