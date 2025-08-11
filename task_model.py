class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.is_done = False  # Atributo conflictivo
        self.removed = False  # Atributo conflictivo

    def get_task_name(self):
        return self.task_name

    def set_done(self):
        self.is_done = True  # Marca la tarea como completada

    def is_done_method(self):
        return self.is_done  # Consulta si la tarea está completada

    def remove_task(self):
        self.removed = True  # Marca la tarea como eliminada

    def is_removed(self):
        return self.removed  # Consulta si la tarea está eliminada
