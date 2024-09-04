import factory

from people.tests.factories import ArtistFactory, OrganizationFactory

from .. import models


class PromotionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Promotion

    name = factory.Faker("catch_phrase")
    starting_year = factory.Faker("year")
    ending_year = factory.Faker("year")


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Student

    number = factory.Faker("random_int")
    promotion = factory.SubFactory(PromotionFactory)
    artist = factory.SubFactory(ArtistFactory)
    user = factory.SelfAttribute("artist.user")


class PhdStudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PhdStudent

    student = factory.SubFactory(StudentFactory)
    university = factory.SubFactory(OrganizationFactory)
    thesis_object = factory.Faker("word")

    @factory.post_generation
    def directors(self, create, extracted, **kwargs):
        if extracted:
            # A list of user were passed in, use them
            for user in extracted:
                self.directors.add(user)


class ScienceStudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ScienceStudent

    student = factory.SubFactory(StudentFactory)
    field = factory.Faker("word")


class TeachingArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TeachingArtist

    artist = factory.SubFactory(ArtistFactory)
    presentation_text_fr = factory.Faker("word")
    presentation_text_en = factory.Faker("word")


class VisitingStudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.VisitingStudent

    number = factory.Faker("random_int")
    promotion = factory.SubFactory(PromotionFactory)
    artist = factory.SubFactory(ArtistFactory)
    user = factory.SelfAttribute("artist.user")
