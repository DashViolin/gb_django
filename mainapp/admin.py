from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


class BaseModelAdmin(admin.ModelAdmin):
    def delete(self, request, queryset):
        for item in queryset:
            item.delete()

    def restore(self, request, queryset):
        for item in queryset:
            item.restore()

    delete.short_description = _("Mark deleted")
    restore.short_description = _("Restore")
    actions = ["delete", "restore"]
    ordering = ["-created"]
    list_per_page = 10


@admin.register(mainapp_models.News)
class NewsAdmin(BaseModelAdmin):
    list_filter = ["created", "deleted"]


@admin.register(mainapp_models.Lessons)
class LessonAdmin(BaseModelAdmin):
    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_filter = ["course", "created", "deleted"]


@admin.register(mainapp_models.Courses)
class LessonAdmin(BaseModelAdmin):
    pass


@admin.register(mainapp_models.Teachers)
class LessonAdmin(BaseModelAdmin):
    pass
