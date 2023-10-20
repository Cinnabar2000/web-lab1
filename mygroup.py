groupmates = [
    {
        "name": "Ирина",
        "surname": "Мезинова",
        "exams": ["КС", "ОЭД", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Максим",
        "surname": "Балашов",
        "exams": ["КС", "РКПО", "СТ"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Надежда",
        "surname": "Сударикова",
        "exams": ["СТ", "РКПО", "ОП"],
        "marks": [5, 5, 5]
    },
        {
        "name": "Полина",
        "surname": "Калещук",
        "exams": ["КС", "ОП", "СП"],
        "marks": [5, 5, 5]
    },    {
        "name": "Игнат",
        "surname": "Еремин",
        "exams": ["СП", "ОЭД", "СТ"],
        "marks": [4, 5, 4]
    },    {
        "name": "Полина",
        "surname": "Вешкина",
        "exams": ["СП", "ОЭД", "СТ"],
        "marks": [4, 5, 5]
    }
]

def filter_students(students) :
    min_mark = float(input("Введите минимальную среднюю оценку студента: "))
    accepted_students = []
    for student in students:
        average_mark = sum(student["marks"])/len(student["marks"])
        if average_mark > min_mark:
            accepted_students.append(student)
    return accepted_students

filtered_students = filter_students(groupmates)
print (
        u"Имя".ljust(15), 
        u"Фамилия".ljust(10), 
        u"Экзамены".ljust(30), 
        u"Оценки".ljust(20))
for student in filtered_students:
    print(
        student["name"].ljust(15), 
        student["surname"].ljust(10), 
        str(student["exams"]).ljust(30), 
        str(student["marks"]).ljust(20)
    )
