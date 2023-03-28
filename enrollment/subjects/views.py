from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import SubjectSerializer, SubjectProfessorSerializer, SubjectStudentSerializer
from .models import Subject, SubjectProfessor, SubjectStudent


class SubjectViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    def get_queryset(self):
        queryset = Subject.objects.all().order_by('date_added')
        return queryset


class SubjectProfessorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = SubjectProfessorSerializer
    queryset = SubjectProfessor.objects.all()

    def get_queryset(self):
        queryset = SubjectProfessor.objects.all().order_by('date_joined')
        return queryset


class SubjectStudentViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = SubjectStudentSerializer
    queryset = SubjectStudent.objects.all()

    def get_queryset(self):
        queryset = SubjectStudent.objects.all().order_by('date_joined')
        return queryset
