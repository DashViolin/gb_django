from typing import Any, Dict, Optional

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView

from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name: str = "mainapp/index.html"


class NewsListView(ListView):
    model = mainapp_models.News
    news_per_page = 10

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = mainapp_models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)


class NewsDetailView(DetailView):
    model = mainapp_models.News


class CoursesListView(TemplateView):
    template_name: str = "mainapp/courses.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class ContactsPageView(TemplateView):
    template_name: str = "mainapp/contacts.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["data"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name: str = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs) -> Dict[str, Any]:
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lessons.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.Teachers.objects.filter(course=context["course_object"])
        return context


class DocSitePageView(TemplateView):
    template_name: str = "mainapp/doc_site.html"


class GoogleRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs) -> Optional[str]:
        domain = "https://www.google.com"
        param = self.request.GET["param"]
        self.url = f"{domain}/search?q={param}"
        return super().get_redirect_url(*args, **kwargs)
