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

def contar_pendientes(tareas):
   contadorPendientes = 0
   for i in tareas:
      if i["hecha"] == False:
         contadorPendientes = contadorPendientes + 1
   print(f"Hay {contadorPendientes} tareas pendientes")


if __name__ == "__main__":

 ListaAgenda = [{"titulo": "Estudiar Python", "hecha": False}, 
                {"titulo": "Hacer ejercicio", "hecha": True},
                {"titulo": "Leer 10 páginas", "hecha": False}]
 
 #Prueba
 #1
 listar_tareas(ListaAgenda)
 #2
 agregar_tareas(ListaAgenda, "Sacar la basura")
 print(ListaAgenda)
 #3
 marcar_hecha(ListaAgenda, "Estudiar Python")
 print(ListaAgenda)
 #4
 listar_tareas(ListaAgenda)



 