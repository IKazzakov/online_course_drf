from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from course_app.models import Course, Lesson
from course_app.permissions import IsOwner, IsModerator
from course_app.serializers import CourseSerializer, LessonSerializer
from users.models import Payments
from users.serializers import PaymentSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    perms_methods = {
        'list': [IsAuthenticated, IsModerator | IsAdminUser],
        'retrieve': [IsAuthenticated, IsOwner | IsModerator | IsAdminUser],
        'create': [IsAuthenticated, ~IsModerator],
        'update': [IsAuthenticated, IsOwner | IsModerator],
        'partial_update': [IsAuthenticated, IsOwner | IsModerator],
        'destroy': [IsAuthenticated, IsOwner | IsAdminUser],
    }

    def get_permissions(self):
        self.permission_classes = self.perms_methods.get(self.action, self.permission_classes)
        return [permission() for permission in self.permission_classes]


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, ~IsModerator]


class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsAdminUser]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'method_payment']
    ordering_fields = ['payment_date']
    permission_classes = [IsModerator | IsOwner]


class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsOwner]


class PaymentDeleteView(generics.DestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsOwner]


class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsModerator | IsOwner]


class PaymentUpdateView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsModerator | IsOwner]
