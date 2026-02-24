def agregar_tareas(tareas, titulo):
    tareas.append({"titulo": titulo, "hecha": False})

def marcar_hecha(tareas, titulo):
    for i in tareas:
        if i["titulo"] == titulo: 
            i["hecha"] = True
        print(f"No se ha encontrado el titulo {titulo}")

def listar_tareas(tareas):
   for i in tareas:
      if i["hecha"] == True:
         print(f"[x]", i["titulo"])
      else:
         print(f"[]", i["titulo"])







if __name__ == "__main__":

 ListaAgenda = [{"titulo": "Estudiar Python", "hecha": False}, 
                {"titulo": "Hacer ejercicio", "hecha": True},
                {"titulo": "Leer 10 páginas", "hecha": False}]
 



 