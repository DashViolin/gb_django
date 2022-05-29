import json

from django.db import models


class MainappModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class MainappBaseModel(models.Model):
    objects = MainappModelManager()

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated", editable=False)
    deleted = models.BooleanField(default=False, verbose_name="Deleted")

    def delete(self, *args):
        self.deleted = True
        self.save()

    def restore(self, *args):
        self.deleted = False
        self.save()

    class Meta:
        abstract = True


class News(MainappBaseModel):
    title = models.CharField(max_length=256, verbose_name="Title")
    preambule = models.CharField(max_length=1024, verbose_name="Preambule")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"


class Courses(MainappBaseModel):
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    description_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Cost")
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"


class Lessons(MainappBaseModel):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Title")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    description_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    class Meta:
        ordering = ("course", "num")


class Teachers(MainappBaseModel):
    courses = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(default=False)

    def __str__(self) -> str:
        return f"{self.pk:0>3} {self.name_second} {self.name_first}"


contacts_data = json.loads(
    """
[
  {
    "links": [
      {
        "name": "Петропавловская крепость",
        "href": "https://yandex.ru/maps/org/petropavlovskaya_krepost/146720535721/?utm_medium=mapframe&utm_source=maps"
      },
      {
        "name": "Достопримечательность в Санкт‑Петербурге",
        "href": "https://yandex.ru/maps/2/saint-petersburg/category/landmark_attraction/89683368508/?utm_medium=mapframe&utm_source=maps"
      },
      {
        "name": "Музей в Санкт‑Петербурге",
        "href": "https://yandex.ru/maps/2/saint-petersburg/category/museum/184105894/?utm_medium=mapframe&utm_source=maps"
      }
    ],
    "frame_link": "https://yandex.ru/map-widget/v1/-/CCUAZHcrhA",
    "title": "Санкт‑Петербург",
    "phone": "+7-999-11-11111",
    "email": "geeklab@spb.ru",
    "address": "территория Петропавловская крепость, 3Ж"
  },
  {
    "links": [
      {
        "name": "Казанский Кремль",
        "href": "https://yandex.ru/maps/org/kazanskiy_kreml/95813866834/?utm_medium=mapframe&utm_source=maps"
      },
      {
        "name": "Музей в Казани",
        "href": "https://yandex.ru/maps/43/kazan/category/museum/184105894/?utm_medium=mapframe&utm_source=maps"
      },
      {
        "name": "Достопримечательность в Казани",
        "href": "https://yandex.ru/maps/43/kazan/category/landmark_attraction/89683368508/?utm_medium=mapframe&utm_source=maps"
      }
    ],
    "frame_link": "https://yandex.ru/map-widget/v1/-/CCUAZHX3xB",
    "title": "Казань",
    "phone": "+7-999-22-22222",
    "email": "geeklab@kz.ru",
    "address": "территория Кремль, 11, Казань, Республика Татарстан, Россия"
  },
  {
    "links": [
      {
        "name": "Собор Покрова Пресвятой Богородицы на Рву",
        "href": "https://yandex.ru/maps/org/sobor_pokrova_presvyatoy_bogoroditsy_na_rvu/175159255687/?utm_medium=mapframe&utm_source=maps"
      },
      {
        "name": "Музей в Москве",
        "href": "https://yandex.ru/maps/213/moscow/category/museum/184105894/?utm_medium=mapframe&utm_source=maps"
      }
    ],
    "frame_link": "https://yandex.ru/map-widget/v1/-/CCUAZHh9kD",
    "title": "Москва",
    "phone": "+7-999-33-33333",
    "email": "geeklab@msk.ru",
    "address": "Красная площадь, 7, Москва, Россия"
  }
]"""
)

news = json.loads(
    """
[
  {
    "title": "Интересаня новость 1",
    "content": "<a href=\\"/mainapp/search-in-google?param=All+work+and+no+play+makes+Jack+a+dull+boy\\" target=\\"_blank\\">All work and no play makes Jack a dull boy</a>\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 2",
    "content": "All work and no play makes Jack a dull boy\\n<a href=\\"/mainapp/search-in-google?param=сияние+фильм\\" target=\\"_blank\\">All work and no play makes Jack a dull boy</a>\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 3",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 4",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 5",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 6",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 7",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 8",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 9",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 10",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 11",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 12",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 13",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 14",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 15",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 16",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 17",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  },
  {
    "title": "Интересаня новость 18",
    "content": "All work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\nAll work and no play makes Jack a dull boy\\n"
  }
]"""
)
