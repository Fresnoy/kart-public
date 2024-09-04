from django.urls import path

from . import views

from kart.urls import router

router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    path("", views.UserViewSet.as_view({"get": "list"})),
]
