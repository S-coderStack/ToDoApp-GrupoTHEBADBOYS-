# ToDoApp-GrupoTHEBADBOYS-

## Integrantes:
- Juan Lubo
- Jonathan Marenco
- Santiago Meriño

## Funcionalidades implementadas por cada estudiante:

### Estudiante 1 Santiago Meriño
- Marcar tareas como completadas.
- Métodos: `mark_as_complete()`, `is_completed()`

### Estudiante 2 Juan Lubo
- Eliminar tareas.
- Método: `delete_task()`

### Estudiante 3 Joanthan Marenco
- Simulación de conflicto: nombres alternativos para atributos y métodos.
- Métodos: `set_done()`, `is_done_method()`, `remove_task()`, `is_removed()`


## Ejemplos de uso

### Marcar tarea como completada (Estudiante 1)
```python
task = TaskModel("Estudiar para el examen")
task.mark_as_complete()
print(task.is_completed())  # True
```

### Eliminar tarea (Estudiante 2)
```python
task = TaskModel("Estudiar para el examen")
task.delete_task()
print(task.is_deleted())  # True
```

### Simulación de conflicto (Estudiante 3)
```python
task = TaskModel("Estudiar para el examen")
task.set_done()
print(task.is_done_method())  # True
task.remove_task()
print(task.is_removed())  # True
```

## Instrucciones de uso
1. Crea una tarea con `TaskModel("nombre de la tarea")`.
2. Marca la tarea como completada con `mark_as_complete()` y verifica con `is_completed()`.
3. Elimina una tarea con el método `delete_task()` y verifica con `is_deleted()`.
4. (Conflicto) Usa los métodos alternativos para simular el conflicto: `set_done()`, `is_done_method()`, `remove_task()`, `is_removed()`.
