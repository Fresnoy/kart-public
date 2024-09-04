from django.conf.urls import include
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from tastypie.api import Api
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from dj_rest_auth.views import PasswordResetConfirmView

from people.api import ArtistResource, StaffResource, OrganizationResource, UserResource
from production.api import (
    InstallationResource,
    FilmResource,
    PerformanceResource,
    EventResource,
    ExhibitionResource,
    ItineraryResource,
    ArtworkResource,
    StaffTaskResource,
)
from diffusion.api import PlaceResource, AwardResource, MetaAwardResource
from school.api import PromotionResource, StudentResource

from people.views import (
    ArtistViewSet,
    ArtistAutocompleteSearchViewSet,
    UserViewSet,
    FresnoyProfileViewSet,
    StaffViewSet,
    OrganizationViewSet,
)
from people import views as people_views
from school.views import (
    PromotionViewSet,
    StudentViewSet,
    PhdStudentViewSet,
    VisitingStudentViewSet,
    ScienceStudentViewSet,
    StudentAutocompleteSearchViewSet,
    TeachingArtistViewSet,
)

from school import views as school_views
from production.views import (
    ArtworkViewSet,
    ArtworkAutocompleteSearchViewSet,
    FilmViewSet,
    InstallationViewSet,
    PerformanceViewSet,
    FilmGenreViewSet,
    InstallationGenreViewSet,
    EventViewSet,
    ItineraryViewSet,
    FilmKeywordsViewSet,
    CollaboratorViewSet,
    PartnerViewSet,
    OrganizationTaskViewSet,
    StaffTaskViewSet,
    ArtworkKeywordsViewSet,
)
from diffusion.views import (
    PlaceViewSet,
    AwardViewSet,
    MetaAwardViewSet,
    MetaEventViewSet,
    DiffusionViewSet,
)
from common.views import BTBeaconViewSet, WebsiteViewSet
from assets.views import GalleryViewSet, MediumViewSet
from assets import views as assets_views

# Graphene
from school.schema_views import (
    PromotionViewGQL,
    StudentViewGQL,
    TeachinArtistListViewGQL,
    TeachingArtistGQL,
)
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(InstallationResource())
v1_api.register(FilmResource())
v1_api.register(PerformanceResource())
v1_api.register(EventResource())
v1_api.register(OrganizationResource())
v1_api.register(StaffTaskResource())
v1_api.register(PromotionResource())
v1_api.register(StudentResource())
v1_api.register(ArtistResource())
v1_api.register(StaffResource())
v1_api.register(UserResource())
v1_api.register(PlaceResource())
v1_api.register(AwardResource())
v1_api.register(MetaAwardResource())
v1_api.register(ExhibitionResource())
v1_api.register(ItineraryResource())
v1_api.register(ArtworkResource())

v2_api = routers.DefaultRouter(trailing_slash=False)
v2_api.register(r"people/user", UserViewSet)
v2_api.register(r"people/userprofile", FresnoyProfileViewSet)
v2_api.register(r"people/artist", ArtistViewSet)
v2_api.register(
    r"people/artist-search",
    ArtistAutocompleteSearchViewSet,
    basename="people-artist-search",
)
v2_api.register(r"school/artist-teacher", TeachingArtistViewSet)
v2_api.register(r"people/staff", StaffViewSet)
v2_api.register(r"people/organization", OrganizationViewSet)
v2_api.register(r"people/organization-staff", OrganizationTaskViewSet)
v2_api.register(r"school/promotion", PromotionViewSet)
v2_api.register(r"school/student", StudentViewSet)
v2_api.register(r"school/phd-student", PhdStudentViewSet)
v2_api.register(r"school/science-student", ScienceStudentViewSet)
v2_api.register(r"school/visiting-student", VisitingStudentViewSet)
v2_api.register(
    r"school/student-search",
    StudentAutocompleteSearchViewSet,
    basename="school-student-search",
)
v2_api.register(r"production/artwork", ArtworkViewSet)
v2_api.register(
    r"production/artwork-keywords", ArtworkKeywordsViewSet, basename="artwork-keywords"
)
v2_api.register(
    r"production/artwork-search",
    ArtworkAutocompleteSearchViewSet,
    basename="production-artwork-search",
)
v2_api.register(r"production/film", FilmViewSet)
v2_api.register(r"production/film-keywords", FilmKeywordsViewSet)
v2_api.register(r"production/event", EventViewSet)
v2_api.register(r"production/itinerary", ItineraryViewSet)
v2_api.register(r"production/film-genre", FilmGenreViewSet)
v2_api.register(r"production/installation", InstallationViewSet)
v2_api.register(r"production/installation-genre", InstallationGenreViewSet)
v2_api.register(r"production/performance", PerformanceViewSet)
v2_api.register(r"production/collaborator", CollaboratorViewSet)
v2_api.register(r"production/partner", PartnerViewSet)
v2_api.register(r"production/task", StaffTaskViewSet)
v2_api.register(r"diffusion/place", PlaceViewSet)
v2_api.register(r"diffusion/meta-award", MetaAwardViewSet)
v2_api.register(r"diffusion/award", AwardViewSet)
v2_api.register(r"diffusion/meta-event", MetaEventViewSet)
v2_api.register(r"diffusion/diffusion", DiffusionViewSet)
v2_api.register(r"common/beacon", BTBeaconViewSet)
v2_api.register(r"common/website", WebsiteViewSet)
v2_api.register(r"assets/gallery", GalleryViewSet)
v2_api.register(r"assets/medium", MediumViewSet)


urlpatterns = (
    [
        # basic Django user account reset password
        path(
            "account/reset_password/",
            auth_views.PasswordResetView.as_view(
                template_name="accounts/reset_password/password_reset_form.html",
                html_email_template_name="accounts/reset_password/password_reset_email.html",
                email_template_name="accounts/reset_password/password_reset_email_txt.html",
                subject_template_name="accounts/reset_password/password_reset_subject.txt",
            ),
            name="reset_password",
        ),
        path(
            "account/reset_password_sent/",
            auth_views.PasswordResetDoneView.as_view(
                template_name="accounts/reset_password/password_reset_sent.html"
            ),
            name="password_reset_done",
        ),
        path(
            "account/reset_password_form/<uidb64>/<token>/",
            auth_views.PasswordResetConfirmView.as_view(
                template_name="accounts/reset_password/password_reset_confirm.html"
            ),
            name="basic_password_reset_confirm",
        ),
        path(
            "account/reset_password_complete/",
            auth_views.PasswordResetCompleteView.as_view(
                template_name="accounts/reset_password/password_reset_complete.html",
            ),
            name="password_reset_complete",
        ),
        # REST API V2
        path("v2/", include(v2_api.urls)),
        path("v2/auth/", obtain_jwt_token, name="obtain-jwt-token"),
        # basic REST context user registration
        path("v2/rest-auth/", include("dj_rest_auth.urls")),
        path("v2/rest-auth/registration/", include("dj_rest_auth.registration.urls")),
        re_path(
            f"v2/rest-auth/password/reset/confirm/{settings.PASSWORD_TOKEN}/",
            PasswordResetConfirmView.as_view(),
            name="password_reset_confirm",
        ),
        # api v1
        path("", include(v1_api.urls)),
        path("grappelli/", include("grappelli.urls")),
        path("admin/", admin.site.urls),
        # Graphene
        path(
            "graphql", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="graphql"
        ),
        path(
            "page/promotionGQL/<int:id>",
            csrf_exempt(PromotionViewGQL.as_view()),
            name="promotionGQL",
        ),
        path(
            "page/promotionsGQL",
            csrf_exempt(PromotionViewGQL.as_view()),
            name="promotionsGQL",
        ),
        path(
            "page/studentGQL/<int:id>",
            csrf_exempt(StudentViewGQL.as_view()),
            name="studentGQL",
        ),
        path(
            "page/studentsGQL",
            csrf_exempt(StudentViewGQL.as_view()),
            name="studentsGQL",
        ),
        # TeachingArtists
        path(
            "page/teachingArtistsList",
            csrf_exempt((TeachinArtistListViewGQL.as_view())),
            name="teachingArtistsList_gql",
        ),
        path(
            "page/teachingArtist/<int:id>",
            csrf_exempt((TeachingArtistGQL.as_view())),
            name="teachingArtist_gql",
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
