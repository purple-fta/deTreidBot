import subprocess

def run_node_script(script_path, *args):
    """
    Запускает Node.js скрипт с переданными аргументами.

    Args:
        script_path (str): Путь к JS файлу.
        *args: Переменное количество аргументов для передачи скрипту.

    Returns:
        tuple: Кортеж, содержащий код возврата (int) и вывод скрипта (str).
               Возвращает None, если произошла ошибка при запуске.
    """
    try:
        command = ['node', script_path] + list(map(str, args))
        process = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', check=True)
        return process.returncode, process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения Node.js скрипта: {e}")
        print(f"stderr: {e.stderr}")
        return e.returncode, e.stderr
    except FileNotFoundError:
        print(f"Ошибка: Файл Node.js не найден по пути: {script_path}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None

