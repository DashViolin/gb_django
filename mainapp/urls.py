from django.urls import path
from django.views.generic import RedirectView

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    # path("", views.HelloWorldVIew.as_view()),
    # path("<str:word>/", views.kwargs_check),
    path("", RedirectView.as_view(url="index")),
    path("index", views.MainPageView.as_view()),
    path("login", views.LoginPageView.as_view()),
    path("news", views.NewsPageView.as_view()),
    path("courses-list", views.CoursesPageView.as_view()),
    path("doc-site", views.DocSitePageView.as_view()),
    path("contacts", views.ContactsPageView.as_view()),
]
