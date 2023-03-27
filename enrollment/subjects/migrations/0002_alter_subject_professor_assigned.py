# Generated by Django 4.1.7 on 2023-03-27 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_alter_professor_age'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='professor_assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='professor.professor'),
        ),
    ]
