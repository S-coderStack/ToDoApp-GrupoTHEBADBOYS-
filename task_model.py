class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.deleted = False  # Nuevo atributo

    def get_task_name(self):
        return self.task_name

    def delete_task(self):
        self.deleted = True  # Marca la tarea como eliminada

    def is_deleted(self):
        return self.deleted  # Consulta si la tarea está eliminada
