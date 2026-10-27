
from datetime import datetime
from django.shortcuts import render


def home(request):
    days = {
        0: ('Понедельник', '#3498db'),
        1: ('Вторник', '#9b59b6'),
        2: ('Среда', '#1abc9c'),
        3: ('Четверг', '#e67e22'),
        4: ('Пятница', '#e74c3c'),
        5: ('Суббота', '#34495e'),
        6: ('Воскресенье', '#f1c40f'),
    }

    today = datetime.today().weekday()
    day_name, background_color = days[today]

    return render(request, 'weekdays/home.html', {
        'day_name': day_name,
        'background_color': background_color,
    })
