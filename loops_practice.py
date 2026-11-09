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

import random
import time

def simulate_load():
    steps_count = 10
    min_val = 0
    max_val = 100
    threshold = 85
    delay = 0.2

    for step in range(steps_count):
        current_load = random.randint(min_val, max_val)
        print(f"Шаг {step +1}: Нагрузка = {current_load}%")

        if current_load > threshold:
            print(f"  ⚠️ ВНИМАНИЕ: Нагрузка {current_load}% превысила порог {threshold}%!")

        time.sleep(delay)
simulate_load()