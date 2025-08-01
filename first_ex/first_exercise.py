import pathlib

def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            salaries = file.readlines()
        salaries = [int(line.strip().split(',')[1]) for line in salaries if line.strip()]
        total = sum(salaries)
        if len(salaries) != 0:
            average = total / len(salaries)
        else:
            average = None
        return (total, average)
    except FileNotFoundError:
        print("Не вдалося знайти файл про заробітні плати розробників")
        return (None, None)

total, average = total_salary(f"{pathlib.Path(__file__).parent}/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")