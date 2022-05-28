from django.urls import path
from django.views.generic import RedirectView

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    # path("", views.HelloWorldVIew.as_view()),
    # path("<str:word>/", views.kwargs_check),
    path("", RedirectView.as_view(url="index")),
    path("index", views.MainPageView.as_view(), name="index"),
    path("login", views.LoginPageView.as_view(), name="login"),
    path("news", views.NewsPageView.as_view(), name="news"),
    path("news/<int:page>", views.NewsPageWithPaginatorView.as_view(), name="news_paginator"),
    path("courses", views.CoursesPageView.as_view(), name="courses"),
    path("doc-site", views.DocSitePageView.as_view(), name="doc-site"),
    path("contacts", views.ContactsPageView.as_view(), name="contacts"),
    path("search-in-google", views.GoogleRedirectView.as_view(), name="search_in_google"),
]
