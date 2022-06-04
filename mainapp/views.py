from math import ceil
from typing import Any, Dict, Optional

from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView

from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name: str = "mainapp/index.html"


class LoginPageView(TemplateView):
    template_name: str = "mainapp/login.html"


class DocSitePageView(TemplateView):
    template_name: str = "mainapp/doc_site.html"


class NewsPageView(TemplateView):
    template_name: str = "mainapp/news.html"
    news_per_page = 5

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        news_count = mainapp_models.News.objects.all().count()
        pages_count = ceil(news_count / self.news_per_page)
        page = int(self.request.GET.get("page", default="1"))
        page = page if page > 0 else 1
        page = page if page <= pages_count else pages_count
        offset = (page - 1) * self.news_per_page
        news = mainapp_models.News.objects.all()
        context["pages"] = range(1, pages_count + 1)
        context["news_qs"] = news[offset : offset + self.news_per_page]
        context["current_page"] = page
        return context


class NewsDetailView(TemplateView):
    template_name: str = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class CoursesListView(TemplateView):
    template_name: str = "mainapp/courses.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name: str = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs) -> Dict[str, Any]:
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lessons.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.Teachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name: str = "mainapp/contacts.html"

    def get_context_data(self, **kwargs: any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["data"] = mainapp_models.contacts_data
        return context


class GoogleRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs) -> Optional[str]:
        domain = "https://www.google.com"
        param = self.request.GET["param"]
        self.url = f"{domain}/search?q={param}"
        return super().get_redirect_url(*args, **kwargs)
