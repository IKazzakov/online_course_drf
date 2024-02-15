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
    lessons = LessonSerializer(many=True, source="lesson_set")
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = (
            "name",
            "preview",
            "description",
            "user",
            "lessons_count",
            "lessons",
        )
