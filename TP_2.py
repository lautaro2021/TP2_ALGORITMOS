moderadores = [ 
    [0, "admin@ayed.com", 333444, "Adrian", "1987-06-24", "Vivo en Miami", "Dar clases de futbol", 'i'],
    ]

estudiantes = [ 
    [0, "estudiante1@ayed.com", 333444, "Leonel", "1987-06-24", "Vivo en Miami", "Dar clases de futbol", 'i'],
    [1, "estudiante2@ayed.com", 555666, "Cristiano", "1985-06-24", "Vivo en Arabia", "Ver clases de futbol", 'i'],
    [2, "estudiante3@ayed.com", 777888, "Alexis", "1999-01-24", "Estudiante de ISI", "Dibujar", 'i'],
    [3, "estudiante4@ayed.com", 999000, "Jorge", "1999-05-01", "Corredor de F1", "Pasear al perro", 'i'],
    []
    ]

usuario_logeado = ["", ""]

###FUNCIONES DE VALIDACION DE DATOS###
def validar_rango(a, b, c):
    if c >= a and c <= b:
        return True
    return False

def validar_si_numero(dato):
    try:
        int(dato)
        return True
    except ValueError:
        return False
    
def validar_usuario(user, password):
    for moderador in moderadores:
        if(moderador[1] == user and moderador[2] == password):
            return True
    for estudiante in estudiantes:
        if(estudiante[1] == user and estudiante[2] == password):
            return True
    return False

###PROCEDIMIENTOS###
def mostrar_opcion_invalida():
    print("Opción o formato no válido. Por favor, intente de nuevo.")

def mostrar_usuario_inexistente():
    print("Usuario inexistente. Por favor, intente de nuevo.")

def mostrar_texto(texto):
    print(
        "====================================\n"
        f"           {texto}                 \n"
        "====================================\n"
    )

def mostrar_menu_inicio_sesion():
    menu = (
        "====================================\n"
        "    Bienvenido a ESTUDIANTESFAPYD   \n"
        "====================================\n"
        "1. Loguearse\n"
        "2. Registrarse\n"
        "===================================="
    )
    print(menu)

###FUNCIONES GENERALES###
def user_pass():
    cont = 0
    while cont < 3:   
        user = input("Ingrese un email: ")
        password = input("Ingrese una contraseña: ")
        if validar_si_numero(password):
            password = int(password)
            if(validar_usuario(user, password)):
                print("Usuario logeado con exito")
            else:
                mostrar_usuario_inexistente()
                cont+=1
        else:
            mostrar_opcion_invalida()
            cont+=1
    print("Se agotaron los intentos de inicio de sesión.")

###FUNCIONES PRINCIPALES
def iniciar_sesion():
    mostrar_menu_inicio_sesion()
    while True:
        seleccionar_opcion = input("Ingrese una opcion: ")
        if validar_si_numero(seleccionar_opcion):
            seleccionar_opcion = int(seleccionar_opcion)
            if validar_rango(1, 2, seleccionar_opcion):         
                match seleccionar_opcion:
                    case 1:
                        mostrar_texto("INICIAR SESION")
                        user_pass()
                    case 2:
                        mostrar_texto("REGISTRARSE")
            else:
                mostrar_opcion_invalida()
        else:
            mostrar_opcion_invalida()

def principal():
    iniciar_sesion()

principal()
    
    