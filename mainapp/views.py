from datetime import datetime
from math import ceil

from django.views.generic import RedirectView, TemplateView

from mainapp.models import contacts_data, news


class MainPageView(TemplateView):
    template_name: str = "mainapp/index.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context


class LoginPageView(TemplateView):
    template_name: str = "mainapp/login.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация"
        return context


class NewsPageView(TemplateView):
    template_name: str = "mainapp/news.html"
    news_count = 5

    def get_context_data(self, page: int = 0, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        self.news_offset = (page - 1) * self.news_count if page else 0
        context["title"] = "Новости"
        context["news"] = news[self.news_offset : self.news_offset + self.news_count]
        context["pages"] = range(1, ceil(len(news) / self.news_count) + 1)
        context["date_time"] = datetime.now()
        return context


class NewsPageWithPaginatorView(NewsPageView):
    def get_context_data(self, page: int, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(page=page, **kwargs)
        return context


class CoursesPageView(TemplateView):
    template_name: str = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Курсы"
        return context


class DocSitePageView(TemplateView):
    template_name: str = "mainapp/doc_site.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Документация"
        return context


class ContactsPageView(TemplateView):
    template_name: str = "mainapp/contacts.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        context["data"] = contacts_data
        return context


class GoogleRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        domain = "https://www.google.com"
        param = self.request.GET["param"]
        self.url = f"{domain}/search?q={param}"
        return super().get_redirect_url(*args, **kwargs)
