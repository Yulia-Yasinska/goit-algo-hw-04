import sys
from pathlib import Path
from colorama import init, Fore
init(autoreset=True)  

def get_color_directory(directory, tab="    "):
    for path in sorted(directory.iterdir()):
        if path.is_dir():
            print(f"{tab}{Fore.BLUE}{path.name}/")
            get_color_directory(path, tab=tab + "    ")
        else:
            print(f"{tab}{Fore.GREEN}{path.name}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Вкажіть шлях до директорії як аргумент командного рядка.")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(f"{Fore.RED}Шлях не існує: {directory}")
        return

    if not directory.is_dir():
        print(f"{Fore.RED}Це не директорія: {directory}")
        return

    if directory.is_file():
        print(f"{Fore.RED}Це файл, а не директорія: {directory}")
        return

    print(f"{Fore.BLUE}{directory.name}")
    get_color_directory(directory)


if __name__ == "__main__":
    main()