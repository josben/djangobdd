Característica: Pagina principal
    Como un usuario
    Quiero registrar personas en el sistema
    Para registrar personas

    Esquema del escenario: Formulario de registro de personas
        Dado que he introducido el nombre <nombre>
        Y el apellido <apellido>
        Y algo acerca de el <about>
        Cuando oprima el boton <button>
        Entonces registro la persona en el sistema

        Ejemplos:
            |    nombre   | apellido  | about        | button |
            | Benjamin    | Perez     | programador  | submit |
            | Annie       |           | laptop       | submit |

