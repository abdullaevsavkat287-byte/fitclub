from django.urls import path
from . import views

app_name = "management"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path(
        "<str:section>/",
        views.records_list,
        name="records"
    ),

    path(
        "<str:section>/add/",
        views.record_form,
        name="add"
    ),

    path(
        "<str:section>/<int:pk>/edit/",
        views.record_form,
        name="edit"
    ),

    path(
        "<str:section>/<int:pk>/delete/",
        views.record_delete,
        name="delete"
    ),
]