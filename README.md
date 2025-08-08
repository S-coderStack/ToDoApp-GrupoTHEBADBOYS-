# ToDoApp-GrupoTHEBADBOYS-

## Integrantes:
- Juan Lubo
- Jonathan Marenco
- Santiago Meriño

## Funcionalidades implementadas:
- Agregar tareas.
- Ver listado de tareas.
- **Eliminar tareas**
 con la función `remove_task(task_name)` en `task_model.py`.

## Funcionalidad de eliminación de tareas

El modelo `TaskModel` ahora incluye métodos para eliminar una tarea y consultar si está eliminada:

- `delete_task()`: Marca la tarea como eliminada.
- `is_deleted()`: Devuelve `True` si la tarea está eliminada, `False` en caso contrario.

**Ejemplo de uso:**

```python
task = TaskModel("Estudiar para el examen")
task.delete_task()
print(task.is_deleted())  # True
```

## Instrucciones de uso:
1. Crea una tarea con `TaskModel("nombre de la tarea")`.
2. Elimina una tarea con el método `delete_task()`.
3. Verifica si la tarea está eliminada con `is_deleted()`.
