days = {
    'Monday': {
        830: 'Громадянська освіта',
        925: 'Фізика',
        1020: 'Математика',
        1125: 'Хімія',
        1230: 'Информатика',
        1325: 'Захист Укр',
        1420: 'История Украины',
    },
    'Friday': {
        1701: 'Test1',
        1702: 'Test2',
        1805: 'Test3'
    }
}


def what_is_lesson_now(day, time):
    for i in days[day]:
        if time <= i:
            return days[day][i]
