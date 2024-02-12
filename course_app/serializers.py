from rest_framework import serializers

from course_app.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "name",
            "description",
            "preview",
            "video",
            "user",
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "name",
            "preview",
            "description",
            "user",
        )
