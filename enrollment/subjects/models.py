from django.db import models
from django.utils.timezone import now
from professor.models import Professor
# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    course_id = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=now, editable=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    professor_assigned = models.ManyToManyField(
        'professor.Professor', through='subjects.SubjectProfessor')

    def __str__(self):
        return self.subject_name


class SubjectProfessor(models.Model):
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    professor_assigned = models.ForeignKey(
        'professor.Professor', on_delete=models.SET_NULL, null=True)
