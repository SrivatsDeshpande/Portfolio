# Generated by Django 4.1.3 on 2022-12-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=150)),
                ('college', models.CharField(max_length=150)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('gpa', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('tech', models.CharField(max_length=150)),
                ('learnings', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
