from datetime import datetime
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions, status, filters, pagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from drf_haystack.filters import HaystackAutocompleteFilter
from drf_haystack.viewsets import HaystackViewSet

from .models import Artist, User, FresnoyProfile, Staff, Organization
from .serializers import (
    ArtistSerializer,
    ArtistAutocompleteSerializer,
    UserSerializer,
    PublicUserSerializer,
    FresnoyProfileSerializer,
    StaffSerializer,
    OrganizationSerializer,
)


# django-guardian anonymous user
try:
    ANONYMOUS_USER_NAME = settings.ANONYMOUS_USER_NAME
except AttributeError:
    ANONYMOUS_USER_NAME = "AnonymousUser"


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff


class UserIsArtistOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.exclude(username=ANONYMOUS_USER_NAME)
    # serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ("=username", "=email")

    def get_serializer_class(self, *args, **kwargs):
        if (
            self.request.user.is_staff
            or self.kwargs
            and self.request.user.pk == int(self.kwargs["pk"])
        ):
            return UserSerializer
        return PublicUserSerializer


class FresnoyProfileViewSet(viewsets.ModelViewSet):
    queryset = FresnoyProfile.objects.all()
    serializer_class = FresnoyProfileSerializer


class CustomPagination(pagination.PageNumberPagination):
    """
    Customize Pagination
    """

    # no limit when page_size not set
    page_size = 100000
    page_size_query_param = "page_size"
    max_page_size = 20
    page_query_param = "page"

    def get_paginated_response(self, data):
        response = Response(data)
        # pagination on headers
        response["count"] = self.page.paginator.count
        response["next"] = self.get_next_link()
        response["previous"] = self.get_previous_link()
        return response


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().distinct()
    serializer_class = ArtistSerializer
    permission_classes = (UserIsArtistOrReadOnly,)
    pagination_class = CustomPagination


class ArtistAutocompleteSearchViewSet(HaystackViewSet):
    index_models = [Artist]
    serializer_class = ArtistAutocompleteSerializer
    filter_backends = [HaystackAutocompleteFilter]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = CustomPagination


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("=user__username",)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
