from django.urls import path
from .views import (
    ShortURLCreateView,ShortURLListView,ShortURLUpdateView, ShortURLDeleteView, redirect_short_url
)

urlpatterns = [
    path("create/", ShortURLCreateView.as_view(), name="create_short_url"),
    path("", ShortURLListView.as_view(), name= "dashboard"),
    path("<int:pk>/edit/", ShortURLUpdateView.as_view(), name="edit_short_url"),
    path("<int:pk>/delete/", ShortURLDeleteView.as_view(), name="delete_short_url"),
    path("s/<str:code>/", redirect_short_url, name="redirect_short_url"),

]

