import pathlib

def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            cats = file.readlines()
        cats = [line.strip().split(',') for line in cats if line.strip()]
        return [{"id": cat[0], "name": cat[1], "age": cat[2]} for cat in cats]
    
    except FileNotFoundError:
        print("Не вдалося знайти файл про котів")
        return []
    
cats_info = get_cats_info(f"{pathlib.Path(__file__).parent}/cats_file.txt")
print(cats_info)