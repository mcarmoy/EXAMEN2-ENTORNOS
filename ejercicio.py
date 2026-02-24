ListaAgenda = [{"titulo": "Estudiar Python", "hecha": False}, 
               {"titulo": "Hacer ejercicio", "hecha": True},
               {"titulo": "Leer 10 páginas", "hecha": False}]

def agregar_tareas(tareas, titulo):
    tareas.append({"titulo": titulo, "hecha": False})
    