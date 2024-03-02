import requests

url = "http://localhost:8000/"

ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_post = url + "agregar_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

ruta_eliminar = url + "eliminar_estudiante"
eliminar_response = requests.request(method="GET", url=ruta_eliminar)
print(eliminar_response.text)

ruta_post = url + "agregar_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

ruta_filtrar_nombre = url + "buscar_estudiante_id/1"
filtrar_nombre_response = requests.request(method="GET", url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

ruta_actualizar = url + "actualizar_estudiante"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
actualizar_response = requests.request(method="POST", url=ruta_actualizar, json=estudiante_actualizado)
print(actualizar_response.text)

ruta_buscar_nombre = url + "buscar_nombres_p"
response_buscar_nombre = requests.request(method="GET", url=ruta_buscar_nombre)
print(response_buscar_nombre.text)

ruta_contar_carreras = url + "ccarrera"
response_contar_carreras = requests.request(method="GET", url=ruta_contar_carreras)
print(response_contar_carreras.text)

ruta_total_estudiantes = url + "testudiantes"
response_total_estudiantes = requests.request(method="GET", url=ruta_total_estudiantes)
print(response_total_estudiantes.text)
