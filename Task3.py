import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізуємо colorama
init(autoreset=True)


def display_directory_structure(path, prefix=""):

    try:
        # Отримуємо список елементів у директорії
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        
        for index, item in enumerate(items):
            is_last = index == len(items) - 1
            
            # Визначаємо символи для форматування
            current_prefix = "└── " if is_last else "├── "
            next_prefix = "    " if is_last else "│   "
            
            # Форматуємо вивід залежно від типу (директорія чи файл)
            if item.is_dir():
                print(f"{prefix}{current_prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                # Рекурсивно обробляємо поддиректорію
                display_directory_structure(item, prefix + next_prefix)
            else:
                print(f"{prefix}{current_prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    
    except PermissionError:
        print(f"{Fore.RED}Помилка: немає прав доступу до директорії {path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Помилка при обробці директорії: {e}{Style.RESET_ALL}")


def main():
    """
    Основна функція скрипту.
    """
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Використання: python hw03.py <шлях_до_директорії>{Style.RESET_ALL}")
        sys.exit(1)
    
    path_str = sys.argv[1]
    path = Path(path_str)
    
    # Перевіряємо чи існує шлях
    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях '{path_str}' не існує.{Style.RESET_ALL}")
        sys.exit(1)
    
    # Перевіряємо чи це директорія
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path_str}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)
    
    # Виводимо ім'я корневої директорії
    print(f"{Fore.CYAN}{path.name}{Style.RESET_ALL}")
    
    # Виводимо структуру директорії
    display_directory_structure(path)


if __name__ == "__main__":
    main()