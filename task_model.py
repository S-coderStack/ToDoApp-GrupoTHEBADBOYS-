class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.is_completed = False  # Renombrado de is_done a is_completed
        self.deleted = False  # Renombrado de removed a deleted

    def get_task_name(self):
        return self.task_name

    def mark_as_complete(self):
        self.is_completed = True  # Marca la tarea como completada

    def is_done_method(self):
        return self.is_completed  # Consulta si la tarea está completada

    def delete_task(self):
        self.deleted = True  # Marca la tarea como eliminada
        #algooooo

    def is_removed(self):
        return self.deleted  # Consulta si la tarea está eliminada
