# Crear una lista para almacenar los libros
libros = []

# Captura de datos desde el teclado
while True:
    # Solicitar los datos del libro
    nombre = input("Nombre del libro: ")
    categoria = input("Categoría: ")
    ano_publicacion = input("Año de publicación: ")
    numero_hojas = input("Número de hojas: ")
    autor = input("Autor: ")

    # Guardar los datos en un diccionario
    libro = {
        "nombre": nombre,
        "categoria": categoria,
        "ano_publicacion": ano_publicacion,
        "numero_hojas": numero_hojas,
        "autor": autor
    }

    # Agregar el libro a la lista de libros
    libros.append(libro)

    # Preguntar al usuario si desea agregar otro libro
    continuar = input("¿Desea agregar otro libro? (s/n): ")
    if continuar.lower() != 's':
        break

# Imprimir el listado de libros
print("\nListado de libros:")
for libro in libros:
    print(f"Nombre: {libro['nombre']}, Categoría: {libro['categoria']}, Año de Publicación: {libro['ano_publicacion']}, Número de Hojas: {libro['numero_hojas']}, Autor: {libro['autor']}")