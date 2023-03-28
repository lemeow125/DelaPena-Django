from rest_framework import serializers
from .models import Subject
from professor.models import Professor
from professor.serializers import ProfessorSerializer


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    date_added = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    # professor_assigned = serializers.PrimaryKeyRelatedField(
    #    queryset=Professor.objects.all(), many=True)

    professor_assigned = serializers.SlugRelatedField(
        queryset=Professor.objects.all(), many=True, slug_field='first_name', allow_null=True)

    class Meta:
        model = Subject
        fields = ('id', 'subject_name',
                  'description', 'course_id', 'professor_assigned', 'date_added')
        read_only_fields = ('id', 'date_added')
