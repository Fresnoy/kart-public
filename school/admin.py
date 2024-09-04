# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import (
    Promotion,
    Student,
    PhdStudent,
    ScienceStudent,
    VisitingStudent,
    TeachingArtist,
)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "number", "promotion", "graduate")
    search_fields = (
        "number",
        "artist__user__first_name",
        "artist__user__last_name",
        "artist__nickname",
    )

    formfield_overrides = {
        models.TextField: {"widget": AdminPagedownWidget},
    }


@admin.register(TeachingArtist)
class TeachingArtistAdmin(admin.ModelAdmin):
    filter_vertical = ("artworks_supervision",)


class PhdStudentAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "defended",
    )
    ordering = ("student",)

    @admin.display(boolean=True)
    def defended(self, obj):
        return obj.thesis_file.name != ""


admin.site.register(Promotion)
admin.site.register(Student, StudentAdmin)
admin.site.register(PhdStudent, PhdStudentAdmin)
admin.site.register(ScienceStudent)
admin.site.register(VisitingStudent)
