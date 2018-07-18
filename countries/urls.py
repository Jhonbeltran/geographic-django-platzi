from django.contrib import admin
from django.urls import path
from countries.views import (CountryDetailView,CountryIdDetailView)

app_name = 'countries'

urlpatterns = [
    path("<int:id>/", CountryIdDetailView.as_view(), name="id_detail"),
    path("<code>/", CountryDetailView.as_view(), name="code_detail"),
]
