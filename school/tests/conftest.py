import pytest

from utils.tests.conftest import *  # noqa

from . import factories


@pytest.fixture
def promotion(db_ready):
    return factories.PromotionFactory()


@pytest.fixture
def student(db_ready):
    return factories.StudentFactory()


@pytest.fixture
def sciencestudent(db_ready):
    return factories.ScienceStudentFactory()


@pytest.fixture
def phdstudent(db_ready):
    return factories.PhdStudentFactory()


@pytest.fixture
def teachingartist(db_ready):
    return factories.TeachingArtistFactory()


@pytest.fixture
def visitingstudent(db_ready):
    return factories.VisitingStudentFactory()
