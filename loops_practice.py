def get_day_name(day: int) -> str:
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье",
    }
    return days.get(day, "Некорректный день")
def find_max_element():
    numbers = list(range(1,10))
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


def stop_on_five():
    for num in list(range(1,8)):
        if num == 5:
            break
        print(f"Число: {num}")

import random
import time


def generate_words():
    words = [f"str{i}" for i in range(10)]
    return words


def simulate_load():
    STEPS_COUNT = 10
    MIN_RANDOM = 0
    MAX_RANDOM = 100
    THRESHOLD = 85
    PAUSE_SECONDS = 0.2

    for step in range(1, STEPS_COUNT + 1):
        value = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(f"Шаг {step}: сгенерировано значени {value}")

        if value > THRESHOLD:
            print(
            f" ВНИАНИЕ: Значение {value} превысило порог {THRESHOLD}!"
            )

        time.sleep(PAUSE_SECONDS)
if __name__ == "__main__":
    print("--- 1. Название дня недели ---")
    print(f"День 3: {get_day_name(3)}")

    print("\n--- 2. Максимум в списке ---")
    print(f"Максимальное число: {find_max_element()}")

    print("\n--- 3.Остановка цикла на 5 ---")
    stop_on_five()

    print("\n--- 4. Генератор списков words ---")
    words = generate_words()
    print(f"Список words: {words}")

    print("\n--- 5. Имитация нагрузки ---")
    simulate_load()
