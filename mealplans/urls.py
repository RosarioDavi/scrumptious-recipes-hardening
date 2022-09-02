from django.urls import path
from .views import (
    MealplanListView,
    MealplanCreateView,
    MealplansDetailView,
    MealplansUpdateView,
    MealplansDeleteView,
)

urlpatterns = [
    path("", MealplanListView.as_view(), name="mealplans_list"),
    path(
        "create/",
        MealplanCreateView.as_view(),
        name="mealplans_create",
    ),
    path("<int:pk>/", MealplansDetailView.as_view(), name="mealplans_detail"),
    path(
        "<int:pk>/edit/", MealplansUpdateView.as_view(), name="mealplans_edit"
    ),
    path(
        "<int:pk>/delete/",
        MealplansDeleteView.as_view(),
        name="mealplans_delete",
    ),
]
