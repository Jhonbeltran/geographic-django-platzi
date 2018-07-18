from django.contrib import admin
from django.urls import path

from continents.views import ContinentsView, ContinentsIdDetailView

urlpatterns = [
    path("", ContinentsView.as_view(), name="continents_home"),
    path("<int:id>/", ContinentsIdDetailView.as_view(), name="continent_id_detail")
]
