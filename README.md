# 📈 Rastreador de Gastos Personales (RGP)

Aplicación de consola en Python para gestionar y hacer seguimiento de tus gastos diarios. Este proyecto fue creado como una herramienta de aprendizaje para dominar conceptos de Python como la programación orientada a funciones, la gestión de bases de datos con SQLite3 y la interacción con el usuario a través de la consola.

---

## 🛠️ Funcionalidades

El RGP te permite realizar las siguientes operaciones:

- **Agregar un nuevo gasto:** Registra la fecha, categoría, monto y una descripción de tus transacciones.
- **Ver todos los gastos:** Muestra un listado de todos los gastos registrados en la base de datos.
- **Actualizar un gasto:** Modifica los detalles de un gasto existente, identificándolo por su ID único.
- **Eliminar un gasto:** Borra un registro de gasto de forma permanente.

---

## 🚀 Cómo Usar la Aplicación

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Clona este repositorio en tu máquina local o descarga el archivo `proyecto-uno.py`.
3.  Abre una terminal o línea de comandos en el directorio del proyecto.
4.  Ejecuta el programa con el siguiente comando:

    ```bash
    python proyecto-uno.py
    ```

5.  El menú de la aplicación se mostrará en la consola, permitiéndote elegir la operación que deseas realizar.

---

## 💻 Tecnologías Utilizadas

- **Python 3:** El lenguaje de programación principal.
- **SQLite3:** Un módulo de Python para gestionar bases de datos relacionales ligeras, que no requiere un servidor.
- **Visual Studio Code:** El editor de codigo fuente.

---

## 📄 Estructura del Proyecto

El proyecto se compone de un único archivo `proyecto-uno.py` que contiene las siguientes funciones:

- `crear_tabla()`: Crea la tabla `gastos` en la base de datos si no existe.
- `agregar_gasto()`: Inserta un nuevo registro de gasto.
- `leer_gastos()`: Recupera y muestra todos los gastos.
- `actualizar_gasto()`: Modifica los datos de un gasto por su ID.
- `eliminar_gasto()`: Borra un registro de gasto por su ID.
- `menu_principal()`: La función principal que gestiona la interacción con el usuario.

---

## 🤝 Contribuciones

Las sugerencias, mejoras y contribuciones son bienvenidas. Siéntete libre de abrir un *issue* o enviar un *pull request* con tus ideas.
Siempre estoy buscando la manera de aprender y mejorar cada aspecto que conozco de programación.
