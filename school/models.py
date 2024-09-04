from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.utils import make_filepath
from people.models import Artist, Organization
from assets.models import Gallery
from production.models import Artwork


class Promotion(models.Model):
    """
    A promotion of students, for at least 2 years.
    """

    class Meta:
        ordering = ["starting_year"]

    name = models.CharField(max_length=255)
    starting_year = models.PositiveSmallIntegerField()
    ending_year = models.PositiveSmallIntegerField()
    picture = models.ImageField(upload_to=make_filepath, blank=True)

    def __str__(self):
        return "{0} ({1}-{2})".format(self.name, self.starting_year, self.ending_year)


class Student(models.Model):
    """
    An artist, part of a promotion, studying for at least 2 years.
    """

    class Meta:
        ordering = ["artist__user__first_name"]

    number = models.CharField(max_length=50, null=True, blank=True)
    promotion = models.ForeignKey(Promotion, null=True, on_delete=models.SET_NULL)
    graduate = models.BooleanField(default=False)
    diploma_mention = models.CharField(
        max_length=150, null=True, blank=True, help_text="Diploma mention"
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    artist = models.OneToOneField(
        Artist, related_name="student", on_delete=models.PROTECT
    )

    def __str__(self):
        if self.artist.nickname:
            return "{0} ({1})".format(self.artist, self.artist.user)
        else:
            return "{0}".format(self.artist)


class TeachingArtist(models.Model):
    """
    Senior artist mentoring a student in the production of an artwork. Can also produce and exhibit a personal artwork.
    """

    class Meta:
        ordering = ["artist"]

    artist = models.OneToOneField(
        Artist, related_name="teacher", null=True, on_delete=models.SET_NULL
    )
    presentation_text_fr = models.TextField(
        null=True,
        blank=True,
        help_text="General orientation text (not only bio) in FRENCH",
    )
    presentation_text_en = models.TextField(
        null=True,
        blank=True,
        help_text="General orientation text (not only bio) in ENGLISH",
    )
    pictures_gallery = models.OneToOneField(
        Gallery,
        blank=True,
        null=True,
        related_name="teachingartist_pictures",
        on_delete=models.CASCADE,
    )
    artworks_supervision = models.ManyToManyField(
        Artwork, related_name="mentoring", blank=True
    )

    def __str__(self):
        return "{0}".format(self.artist)


class ScienceStudent(models.Model):
    """
    Scientist specialized in a field. Attends Le Fresnoy at least one year. Produces artworks.
    """

    class Meta:
        ordering = ["student"]

    student = models.OneToOneField(
        Student, related_name="science_student", on_delete=models.PROTECT
    )
    field = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.student)


class PhdStudent(models.Model):
    """
    At Le Fresnoy, a PhD student accomplishes an extra year (2+1). Their artworks are part of their thesis.
    """

    class Meta:
        ordering = ["student"]

    student = models.OneToOneField(
        Student, related_name="phd_student", on_delete=models.PROTECT
    )
    university = models.ForeignKey(
        Organization, related_name="phd_student", on_delete=models.PROTECT, blank=True
    )
    directors = models.ManyToManyField(
        User,
        related_name="phd_student",
        blank=True,
    )
    thesis_object = models.CharField(max_length=255, null=True, blank=True)
    thesis_file = models.FileField(
        upload_to=make_filepath, null=True, blank=True, help_text="thesis pdf file"
    )

    def __str__(self):
        return "{0}".format(self.student)


class VisitingStudent(models.Model):
    """
    Visiting student included in a promotion but not eligible for degree.
    """

    class Meta:
        ordering = ["artist"]

    number = models.CharField(max_length=50, null=True, blank=True)
    promotion = models.ForeignKey(Promotion, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    artist = models.OneToOneField(
        Artist, related_name="visiting_student", on_delete=models.PROTECT
    )

    def __str__(self):
        return "{0} ({1})".format(self.user, self.number)
