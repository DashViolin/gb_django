from django.views.generic import TemplateView

# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# from django.views.generic import View


# class HelloWorldVIew(View):
#     def get(self, *args, **kwargs):
#         return HttpResponse("HW!")


# def kwargs_check(request: HttpRequest, **kwargs):
#     return HttpResponse(f"kwargs:<br>{kwargs}")


class MainPageView(TemplateView):
    template_name: str = "mainapp/index.html"


class LoginPageView(TemplateView):
    template_name: str = "mainapp/login.html"


class NewsPageView(TemplateView):
    template_name: str = "mainapp/news.html"


class CoursesPageView(TemplateView):
    template_name: str = "mainapp/courses_list.html"


class DocSitePageView(TemplateView):
    template_name: str = "mainapp/doc_site.html"


class ContactsPageView(TemplateView):
    template_name: str = "mainapp/contacts.html"
