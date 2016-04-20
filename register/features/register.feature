# language: es

Característica: Pagina principal
    Como un usuario
    Quiero registrar personas en el sistema
    Para registrar personas

    Esquema del escenario: Formulario de registro de personas
        Dado que ingreso al sistema con el url "http://127.0.0.1:8000/register/"
        Y voy a la opcion "Nuevo registro"
        Y empiezo introduciendo el nombre <nombre>
        Y el apellido <apellido>
        Y algo acerca de el <about>
        Cuando oprima el boton <button>
        Entonces registro la persona en el sistema

        Ejemplos:
            |    nombre   | apellido  | about        | button  |
            | Benjamin    | Perez     | programador  | Guardar |
            | Annie       | MacBook   | laptop       | Guardar |

