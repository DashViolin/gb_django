from django.urls import path
from django.views.generic import RedirectView

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", RedirectView.as_view(url="index")),
    path("index", views.MainPageView.as_view(), name="index"),
    path("news", views.NewsPageView.as_view(), name="news"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),
    path("courses", views.CoursesListView.as_view(), name="courses"),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail"),
    path("doc_site", views.DocSitePageView.as_view(), name="doc_site"),
    path("contacts", views.ContactsPageView.as_view(), name="contacts"),
    path("search-in-google", views.GoogleRedirectView.as_view(), name="search_in_google"),
]
