from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_testing import settings
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, value):
        if len(value) > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError('Превышено количество студентов(20)')
        return value
