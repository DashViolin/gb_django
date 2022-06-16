from datetime import date
from typing import Any, Dict, Optional

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView

from mainapp import forms as mainapp_forms
from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name: str = "mainapp/index.html"


class NewsListView(ListView):
    model = mainapp_models.News
    paginate_by = 5
    date_from = ""
    date_to = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "form_data": {
                    "dateFrom": self.date_from,
                    "dateTo": self.date_to,
                }
            }
        )
        return context

    def get_queryset(self):
        query_set = super().get_queryset().filter(deleted=False)
        if self.date_from and self.date_to:
            query_set = query_set.filter(
                created__gt=date.fromisoformat(self.date_from),
                created__lt=date.fromisoformat(self.date_to),
            )
        elif self.date_from:
            query_set = query_set.filter(created__gt=date.fromisoformat(self.date_from))
        elif self.date_to:
            query_set = query_set.filter(created__lt=date.fromisoformat(self.date_to))
        return query_set

    def get(self, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        self.date_from = self.request.POST.get("dateFrom", "")
        self.date_to = self.request.POST.get("dateTo", "")
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)


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


class CoursesDetailView(TemplateView):
    template_name: str = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs) -> Dict[str, Any]:
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lessons.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.Teachers.objects.filter(course=context["course_object"])
        if (
            not self.request.user.is_anonymous
            and not mainapp_models.CourseFeedback.objects.filter(
                course=context["course_object"], user=self.request.user
            ).count()
        ):
            context["feedback_form"] = mainapp_forms.CourseFeedbackForm(
                course=context["course_object"],
                user=self.request.user,
            )
        context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
            course=context["course_object"]
        ).order_by("-created", "-rating")[:5]
        return context


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp_models.CourseFeedback
    form_class = mainapp_forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string("mainapp/includes/feedback_card.html", context={"item": self.object})
        return JsonResponse({"card": rendered_card})


class ContactsPageView(TemplateView):
    template_name: str = "mainapp/contacts.html"

    def get_context_data(self, **kwargs: any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["data"] = mainapp_models.contacts_data
        return context


class DocSitePageView(TemplateView):
    template_name: str = "mainapp/doc_site.html"


class GoogleRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs) -> Optional[str]:
        domain = "https://www.google.com"
        param = self.request.GET["param"]
        self.url = f"{domain}/search?q={param}"
        return super().get_redirect_url(*args, **kwargs)
