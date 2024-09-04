import pytest


@pytest.mark.django_db
class TestPromotion:
    def test_str(self, promotion):
        promotion_str = str(promotion)
        assert promotion.name in promotion_str
        assert str(promotion.starting_year) in promotion_str
        assert str(promotion.ending_year) in promotion_str


@pytest.mark.django_db
class TestStudent:
    def test_str(self, student):
        student_str = str(student)
        assert str(student.user) in student_str
        assert str(student.artist.nickname) in student_str


@pytest.mark.django_db
class TestPhdStudent:
    def test_str(self, phdstudent):
        phdstudent_str = str(phdstudent)
        assert str(phdstudent.student.user) in phdstudent_str


@pytest.mark.django_db
class TestScienceStudent:
    def test_str(self, sciencestudent):
        sciencestudent_str = str(sciencestudent)
        assert str(sciencestudent.student.user) in sciencestudent_str


@pytest.mark.django_db
class TestTeachingArtist:
    def test_str(self, teachingartist):
        teachingartist_str = str(teachingartist)
        assert str(teachingartist.artist) in teachingartist_str


@pytest.mark.django_db
class TestVisitingStudent:
    def test_str(self, visitingstudent):
        visitingstudent_str = str(visitingstudent)
        assert str(visitingstudent.artist.user) in visitingstudent_str
