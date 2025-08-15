# main.py
from task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"¿Tarea completada?: {task.is_done_method()}")
    task.delete_task()
    print(f"¿Tarea eliminada?: {task.is_removed()}")

if __name__ == "__main__":
    main()
