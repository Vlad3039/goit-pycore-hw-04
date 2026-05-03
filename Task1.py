def total_salary(path):

    # Аналізує файл із заробітними платами та повертає загальну та середню суму.
    
    try:
        total = 0
        count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    name = parts[0]
                    salary = int(parts[1])
                    total += salary
                    count += 1
        
        if count == 0:
            return 0, 0
        
        average = total / count
        return total, average
    
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 0, 0
    except (ValueError, IndexError) as e:
        print(f"Помилка: неправильний формат даних у файлі. {e}")
        return 0, 0
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")