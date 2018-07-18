from django.contrib import admin
from django.urls import path
from continents.views import ContinentsView, ContinentsIdDetailView

app_name='continents'

urlpatterns = [
    path("", ContinentsView.as_view(), name="home"),
    path("<int:id>/", ContinentsIdDetailView.as_view(), name="id_detail")
]
