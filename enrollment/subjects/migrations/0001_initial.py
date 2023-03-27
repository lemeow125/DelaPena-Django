# Generated by Django 4.1.7 on 2023-03-27 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('course_id', models.CharField(max_length=20)),
                ('professor_assigned', models.CharField(default='', max_length=40, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
