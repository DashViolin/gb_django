# Create your models here.
import json

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
