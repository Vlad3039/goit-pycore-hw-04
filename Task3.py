import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def display_directory_structure(path, prefix=""):
    """
    Рекурсивно відображає структуру директорії з кольоровим виведенням.
    """
    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        
        for index, item in enumerate(items):
            is_last = index == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            next_prefix = "    " if is_last else "│   "
            
            if item.is_dir():
                print(f"{prefix}{current_prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
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
    
    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях '{path_str}' не існує.{Style.RESET_ALL}")
        sys.exit(1)
    
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path_str}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)
    
    print(f"{Fore.CYAN}{path.name}{Style.RESET_ALL}")
    display_directory_structure(path)


if __name__ == "__main__":
    main()