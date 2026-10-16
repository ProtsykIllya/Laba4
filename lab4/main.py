from func_requests import get_status
from func_numpy import matrix_stats
from func_pandas import build_dataframe
from func_matplotlib import save_plot
from func_colorama import print_colored
from func_rich import show_table
from func_tqdm import run_progress
from func_faker import generate_person
from func_pyfiglet import make_banner
from func_dateutil import days_until
from func_math import circle_area
from func_random import random_numbers
from func_json import save_json
from func_os import prepare_folder
from func_datetime import current_time

def main():
    print(make_banner("LAB 4"))
    print_colored("Лабораторна робота 4 запущена", "green")
    print("Поточний час:", current_time())
    print("Днів до дедлайну:", days_until(2026, 10, 16))

    folder = prepare_folder("output")

    print("HTTP статус example.com:", get_status("https://example.com"))
    print("Сума після прогресу:", run_progress(200000))

    people = [generate_person() for _ in range(5)]
    df = build_dataframe(people)
    show_table(df)
    save_json(people, f"{folder}/people.json")

    numbers = random_numbers(20, 1, 100)
    print("Статистика матриці:", matrix_stats(3))
    save_plot(numbers, f"{folder}/plot.png")
    print("Площа кола r=5:", circle_area(5))

    print_colored("Готово! Файли збережено в папці output", "cyan")


if __name__ == "__main__":
    main()