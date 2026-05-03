def get_cats_info(path):
    """
    Читає інформацію про котів з файлу і повертає список словників.
    """
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    
                    if len(parts) < 3:
                        print(f"Попередження: неправильний формат рядка: {line}")
                        continue
                    
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_dict)
        
        return cats_info
    
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    for cat in cats_info:
        print(cat)