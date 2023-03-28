from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_queryset(self):
        queryset = Student.objects.all().order_by('date_joined')
        return queryset
