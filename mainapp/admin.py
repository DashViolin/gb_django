from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(mainapp_models.Lessons)
class LessonAdmin(admin.ModelAdmin):
    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def delete(self, request, queryset):
        # queryset.update(deleted=True)
        for item in queryset:
            item.delete()

    def restore(self, request, queryset):
        # queryset.update(deleted=False)
        for item in queryset:
            item.restore()

    delete.short_description = _("Mark deleted")

    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ["course", "created", "deleted"]
    actions = [delete.__name__, restore.__name__]
