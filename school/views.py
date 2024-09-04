from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, filters
from drf_haystack.viewsets import HaystackViewSet

from dj_rest_auth.views import PasswordResetView


from .models import (
    Promotion,
    Student,
    PhdStudent,
    ScienceStudent,
    TeachingArtist,
    VisitingStudent,
)

from .serializers import (
    PromotionSerializer,
    StudentSerializer,
    PhdStudentSerializer,
    ScienceStudentSerializer,
    TeachingArtistSerializer,
    VisitingStudentSerializer,
    StudentAutocompleteSerializer,
)


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    )


class PhdStudentViewSet(viewsets.ModelViewSet):
    queryset = PhdStudent.objects.all()
    serializer_class = PhdStudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ScienceStudentViewSet(viewsets.ModelViewSet):
    queryset = ScienceStudent.objects.all()
    serializer_class = ScienceStudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TeachingArtistViewSet(viewsets.ModelViewSet):
    queryset = TeachingArtist.objects.all().distinct()
    serializer_class = TeachingArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class VisitingStudentViewSet(viewsets.ModelViewSet):
    queryset = VisitingStudent.objects.all()
    serializer_class = VisitingStudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StudentAutocompleteSearchViewSet(HaystackViewSet):
    index_models = [Student]
    serializer_class = StudentAutocompleteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
