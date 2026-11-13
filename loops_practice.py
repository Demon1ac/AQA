import random
import time


def get_day_name(day: int) -> str:
    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Втоник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "Неверный день недели"


print(get_day_name(3))

numbers = list(range(1, 10))
max_value = numbers[0]

for n in numbers:
    if n > max_value:
        max_value = n
print(f"Максимум: {max_value}")

for n in list(range(1, 8)):
    print(n)
    if n == 5:
        break

words = [f"str{i}" for i in range(10)]
print(words)


def simulate_load():
    steps_count = 10
    min_val = 0
    max_val = 100
    threshold = 85
    delay = 0.2

    for step in range(steps_count):
        current_load = random.randint(min_val, max_val)
        print(f"Шаг {step + 1}: Нагрузка = {current_load}%")

        if current_load > threshold:
            print(
                f"  ⚠️ ВНИМАНИЕ: "
                f"Нагрузка {current_load}% превысила порог {threshold}%!"
            )

        time.sleep(delay)


simulate_load()


class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self) -> None:
        print(f"{self.brand} {self.model} {self.year}")


car1 = Car("BMW", "M4", 2020)
car2 = Car("TOYOTA", "AVENSIS", 2000)
car3 = Car("Mazda", "3", 2017)

car1.print_car_info()
car2.print_car_info()
car3.print_car_info()


class Lead:
    def __init__(self, name: str):
        self.name = name


def change_name(lead: Lead, new_name: str) -> None:
    lead.name = new_name


lead = Lead("Геральт")
print(lead.name)

change_name(lead, "Весемир")
print(lead.name)  # Объект Lead относится к ссылочному типу данных.
# Когда мы передаем его в функцию,
# Питон не создает его копию, а передаёт ссылку на тот же самый объект.
# Поэтому изменение внутри функции меняет исходный объект и это видно снаружи


class Student:
    def __init__(self, name: str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


students = [
    Student("Harry Potter", 11, [4.1, 5.0, 3.2]),
    Student("Ron Weasley", 11, [3.2, 3.0, 3.8]),
    Student("Hermione Granger", 11, [4.5, 4.3, 4.7]),
    Student("Neville Longbottom", 12, []),
]

MIN_AVG = 4.1
best_students = [s for s in students if s.get_avg_grade() > MIN_AVG]

for student in best_students:
    print(f"Студент: {student.name}, " f"ср.бал:{student.get_avg_grade():.2f}")
