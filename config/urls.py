
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Задание 1 — спортивный сайт
    path('', include('sports.urls')),

    # Задание 2 — автомобильный сайт
    path('cars/', include('cars.urls')),

    # Задание 3 — дни недели
    path('weekdays/', include('weekdays.urls')),
]
