#Rastreador de Gastos Personales(RGP)

#Paso 1: Importamos los modulos a utilizar.
import sqlite3

#Función para crear la tabla.
def crear_tabla():
    
    with sqlite3.connect("gastos.db") as connection: # with para gestionar la conexion de forma segura y automatica.
        cursor = connection.cursor()
        #Creamos la tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gastos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                categoria TEXT NOT NULL,
                monto REAL NOT NULL,
                descripcion TEXT
            );
        """)
        print("Tabla 'gastos' creada exitosamente.")
        

#Creamos función para agregar gastos.
def agregar_gasto (fecha, categoria, monto, descripcion):
    try:
        with sqlite3.connect('gastos.db') as connection:
            cursor = connection.cursor()
            
            #SQL con marcadores de posición (?)
            sql_insertar = """
            INSERT INTO gastos(fecha, categoria, monto, descripcion)
            VALUES (?, ?, ?, ?);
        """
            #Tupla con los datos a ingresar.
            datos_gastos = (fecha, categoria, monto, descripcion)
            
            #Ejecutamos la sentencia y pasamos los datos de forma segura.
            cursor.execute(sql_insertar, datos_gastos)
            print("Gasto agregado exitosamente. ")
    except sqlite3.Error as e:
        print(f"Ocurrió un error: {e}")
        

def leer_gastos():
    try:
        with sqlite3.connect('gastos.db') as connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT * FROM gastos;") #Le decimos a la base de datos que columnas queremos obtener y de donde obtenerlas.
            
            #Obtenemos todas las filas con fetchall
            gastos = cursor.fetchall()
            
            #Verificamos si hay gastos para mostrar
            if gastos:
                print("\n LISTA DE GASTOS ")
                for gasto in gastos:
                    #"Cada gasto es una tupla"
                    print(f'ID: {gasto[0]}, Fecha: {gasto[1]}, Categoría: {gasto[2]}, Monto: {gasto[3]}, Descripción: {gasto[4]}')
                print("-------------------------------")
            else:
                print("No hay gastos registrados.")
    except sqlite3.Error as e:
        print(f'Ocurrió un error: {e}')
        
def actualizar_gasto (id_gasto, nueva_fecha, nueva_categoria, nuevo_monto, nueva_descripcion):
    try:
        with sqlite3.connect('gastos.db') as connection:
            cursor = connection.cursor()
            
            #Elegimos los datos a actualizar.
            sql_actualizar = """
                UPDATE gastos
                SET monto = ?, descripcion = ?, categoria = ?, fecha = ?
                WHERE id = ?;
                """
            datos_actualizados = (nuevo_monto, nueva_descripcion,nueva_categoria,nueva_fecha, id_gasto)
            
            cursor.execute(sql_actualizar, datos_actualizados)
            print(f"Gasto con ID {id_gasto} actualizado exitosamente.")
    except sqlite3.Error as e:
        print(f"Ocurrió un error al actualizar: {e}")

def eliminar_gasto(id_gasto):
    try:
        with sqlite3.connect('gastos.db') as connection:
            cursor = connection.cursor()
        
            #Elegimos los datos a eliminar por el número de ID.
            sql_eliminar = "DELETE FROM gastos WHERE id = ?;"
            cursor.execute(sql_eliminar, (id_gasto,))
            print(f"Gasto con ID {id_gasto} eliminado exitosamente.")
    except sqlite3.Error as e:
        print(f"Ocurrió un error al eliminar: {e}")
                
#Creamos la función para el menú principal.
def menu_principal():
    while True:
        print("\n Rastreador de Gastos Personales.")
        print("1.- Agregar Gasto.")
        print("2.- Ver Gastos.")
        print("3.- Actualizar Gastos.")
        print("4.- Eliminar Gastos.")
        print("5.- Salir")
        
        opcion = int(input("Elija una opción (1-5).\n"))
        
        if opcion == 1:
            fecha = str(input("Ingrese la fecha (DD/MM/YYYY): "))
            categoria = str(input("Ingrese la categoria del gasto: "))
            monto = float(input("Ingrese el monto: "))
            descripcion = str(input("Ingrese una descripción al gasto: "))
            agregar_gasto(fecha, categoria, monto, descripcion)
            print("Gasto agregado correctamente.")
        elif opcion == 2:
            leer_gastos()
        elif opcion == 3:
            id_gasto = int(input("Ingrese el ID del gasto a actualizar: \n"))
            nueva_fecha = str(input("Ingrese la nueva fecha del gasto: \n"))
            nueva_categoria = str(input("Ingrese la nueva categoria: \n"))
            nuevo_monto = float(input("Ingrese el nuevo monto: \n"))
            nueva_descripcion = str(input("Ingrese la nueva descripción: \n"))
            actualizar_gasto(id_gasto, nueva_fecha, nueva_categoria, nuevo_monto, nueva_descripcion)
            print("Gasto actualizado correctamente.")
        elif opcion == 4:
            id_gasto = int(input("Ingrese el ID del gasto: \n"))
            eliminar_gasto(id_gasto)
            print("Gasto eliminado correctamente.")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 5.")
        

    
#Puesta en marcha.
if __name__ == "__main__":
    menu_principal()