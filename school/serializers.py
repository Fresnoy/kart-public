from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializerMixin
from dj_rest_auth.serializers import PasswordResetSerializer

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

from people.serializers import PublicUserSerializer

from .models import (
    Promotion,
    Student,
    PhdStudent,
    ScienceStudent,
    TeachingArtist,
    VisitingStudent,
)
from .search_indexes import StudentIndex


class PhdStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhdStudent
        fields = "__all__"


class ScienceStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScienceStudent
        fields = "__all__"


class VisitingStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VisitingStudent
        fields = "__all__"


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # depth = 1

    user_infos = PublicUserSerializer(source="user", read_only=True)
    phd_student = PhdStudentSerializer(
        required=False,
    )
    science_student = ScienceStudentSerializer(
        required=False,
    )

    user = serializers.HyperlinkedRelatedField(
        view_name="user-detail", queryset=User.objects.all(), write_only=True
    )


class TeachingArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeachingArtist
        fields = "__all__"


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"


class StudentAutocompleteSerializer(HaystackSerializerMixin, StudentSerializer):
    class Meta(StudentSerializer.Meta):
        index_classes = [StudentIndex]
        search_fields = ("content_auto",)
        fields = [
            "url",
            "number",
            "graduate",
            "promotion",
            "artist",
            "user",
        ]
        field_aliases = {"q": "content_auto"}
        depth = 1

    user = PublicUserSerializer()
