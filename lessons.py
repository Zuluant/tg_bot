from datetime import datetime
days = {
    'Monday': {
        830: 'Громадянська освіта',
        925: 'Фізика',
        1020: 'Математика',
        1125: 'Хімія',
        1230: 'Інформатика',
        1325: 'Захист України',
        1420: 'Історія України',
    },
    'Friday': {
        1730: 'Інформатика',
        1735: 'Захист України',
        1740: 'Історія України',
    }
}


def what_is_lesson_now(day, time):
    for i in days[day]:
        if time <= i:
            return days[day][i]
    return 'Уроков больше нету!'
