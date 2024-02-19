from django.contrib import admin

# Register your models here.
from course_app.models import Course, Lesson


from course_app.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'description', 'user')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'description', 'video', 'course', 'user')
