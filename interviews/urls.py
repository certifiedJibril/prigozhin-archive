from django.urls import path
from .views import home_view, search_view, test_view

urlpatterns = [
    path("", home_view, name="home"),
    path("search/", search_view, name="search"),
    path("test/", test_view),  # extra
]
