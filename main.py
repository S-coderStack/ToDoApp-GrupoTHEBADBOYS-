# main.py
from task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.delete_task()
    print(f"Tarea eliminada?: {task.is_deleted()}")

if __name__ == "__main__":
    main()
