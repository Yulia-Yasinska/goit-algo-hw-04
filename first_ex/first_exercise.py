import pathlib

current_dir = pathlib.Path(__file__).parent

def total_salary(path):
    try:
        with open(current_dir / path, 'r', encoding="utf-8") as file:
            salaries = file.readlines()
        salaries = [int(line.strip().split(',')[1]) for line in salaries if line.strip()]
        total = int(sum(salaries))
        average = int(total / len(salaries))
        return (total, average)
    except FileNotFoundError:
        print("Не вдалося знайти файл про заробітні плати розробників")
        return (None, None)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")