import pytest

from django.urls import reverse

from people.tests.conftest import *  # noqa
from utils.tests.utils import (
    IsAuthenticatedOrReadOnlyModelViewSetMixin,
    HelpTestForModelViewSet,
    parametrize_user_roles,
)


def pytest_generate_tests(metafunc):
    # pytest hook; called once per each test function
    parametrize_user_roles(metafunc)


@pytest.mark.django_db
class TestPromotionViewSet(
    IsAuthenticatedOrReadOnlyModelViewSetMixin, HelpTestForModelViewSet
):
    viewset_name = "school/promotion"

    fixtures = ["promotion", "user"]

    expected_list_size = 1
    expected_fields = ["starting_year", "ending_year"]

    mutate_fields = ["name"]
    put_fields = ["name", "starting_year", "ending_year"]


@pytest.mark.django_db
class TestStudentViewSet(
    IsAuthenticatedOrReadOnlyModelViewSetMixin, HelpTestForModelViewSet
):
    viewset_name = "school/student"

    fixtures = ["student", "user", "artist"]

    expected_list_size = 1
    expected_fields = ["number", "promotion"]

    mutate_fields = ["number"]
    put_fields = ["artist", "user"]
    built_fields = {
        "artist": lambda x: reverse("artist-detail", kwargs={"pk": x.artist.pk}),
        "user": lambda x: reverse("user-detail", kwargs={"pk": x.user.pk}),
    }

    def get_data(self, field):
        if field in self.built_fields:
            return self.built_fields[field](self)
        else:
            return super().get_data(field)
