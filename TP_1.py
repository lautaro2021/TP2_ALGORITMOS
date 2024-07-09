
from datetime import datetime
import math
import getpass
import sys

#constantes alumnos
#email => string, contraseña => int
estudiante1_email = 'estudiante1@ayed.com'
estudiante1_contraseña = 111222

estudiante2_email = 'estudiante2@ayed.com'
estudiante2_contraseña = 333444

estudiante3_email = 'estudiante3@ayed.com'
estudiante3_contraseña = 555666

#constante fecha
fecha_actual = str(datetime.today().date())

#variables alumnos
#nombre, fecha, biografia, hobbies => string
estudiante1_nombre = 'Lautaro'
estudiante1_fecha = '1999-06-11'
estudiante1_biografia = 'Jugador de futbol frustado'
estudiante1_hobbies = 'Tocar la guitarra'

estudiante2_nombre = 'Leo Messi'
estudiante2_fecha = '1987-06-24'
estudiante2_biografia = 'En Miami de paseo'
estudiante2_hobbies = 'Dar clases de futbol'

estudiante3_nombre = 'Cristiano'
estudiante3_fecha = '1985-02-05'
estudiante3_biografia = 'En Arabia farmeando goles'
estudiante3_hobbies = 'Ver clases de Leo'

#variables funciones
#contador_login => int, usuario_logueado => string, opcion_menu => int, usuario_likeado => string
contador_login = 0
usuario_logueado = ''
opcion_menu = 9
usuario_likeado = ''

#Funciones
#fecha => string
def obtener_edad(fecha):
    fecha_actual_date = datetime.strptime(fecha_actual, '%Y-%m-%d')
    fecha_date = datetime.strptime(fecha, '%Y-%m-%d')
    
    diferencia = fecha_actual_date - fecha_date

    return abs(math.floor(diferencia.days/365))

#Retorna un string en formato YYYY-MM-DD
def verificar_y_corregir_fecha():
    while True:
        fecha = input("Ingrese nueva fecha en formato YYYY-MM-DD: ")
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            print("""
                  Datos actualizados con éxito
                  """)
            return fecha
        except:
            print("La fecha debe tener el formato YYYY-MM-DD")

#Muestra todos los candidatos y permite matchear con uno
def mostrar_candidatos():
    global usuario_likeado
    print("""
          -ESTUDIANTE 1-
          """)
    print("Nombre: ", estudiante1_nombre or 'No existe nombre en base de datos')
    print("Fecha de nacimiento: ", estudiante1_fecha or 'No existe fecha de nacimiento en base de datos')
    print("Edad: ", obtener_edad(estudiante1_fecha), "años")
    print("Biografia: ", estudiante1_biografia or 'No existe biografia en base de datos')
    print("Hobbies: ", estudiante1_hobbies or 'No existen hobbies en base de datos')
    
    print("""
          -ESTUDIANTE 2-
          """)
    print("Nombre: ", estudiante2_nombre or 'No existe nombre en base de datos')
    print("Fecha de nacimiento: ", estudiante2_fecha or 'No existe fecha de nacimiento en base de datos')
    print("Edad: ", obtener_edad(estudiante2_fecha), "años")
    print("Biografia: ", estudiante2_biografia or 'No existe biografia en base de datos')
    print("Hobbies: ", estudiante2_hobbies or 'No existen hobbies en base de datos')
    
    print("""
          -ESTUDIANTE 3-
          """)
    print("Nombre: ", estudiante3_nombre or 'No existe nombre en base de datos')
    print("Fecha de nacimiento: ", estudiante3_fecha or 'No existe fecha de nacimiento en base de datos')
    print("Edad: ", obtener_edad(estudiante3_fecha), "años")
    print("Biografia: ", estudiante3_biografia or 'No existe biografia en base de datos')
    print("Hobbies: ", estudiante3_hobbies or 'No existen hobbies en base de datos')
    
    while True:
        like = input("Ingrese el nombre del estudiante a matchear: ")
        
        if(like != estudiante1_nombre and like != estudiante2_nombre and like != estudiante3_nombre):
            print("El nombre ingresado no existe en nuestra base de datos")
            continue
        
        else:
            usuario_likeado = like
            print("######")
            print("Usuario likeado con exito")
            print("######")
            break

#Permite editar los datos del usuario logeado
def editar_datos():
    print(
        """
          -Editar mis datos personales-
        """)
    if(usuario_logueado == estudiante1_email):
        global estudiante1_nombre
        global estudiante1_biografia
        global estudiante1_hobbies
        global estudiante1_fecha
        
        estudiante1_nombre = input("Ingrese nuevo nombre: ")
        estudiante1_biografia = input("Ingrese nueva biografia: ")
        estudiante1_hobbies = input("Ingrese nuevos hobbies: ")
        estudiante1_fecha = verificar_y_corregir_fecha()

    elif(usuario_logueado == estudiante2_email):
        global estudiante2_nombre
        global estudiante2_biografia
        global estudiante2_hobbies
        global estudiante2_fecha
        
        estudiante2_nombre = input("Ingrese nuevo nombre: ")
        estudiante2_biografia = input("Ingrese nueva biografia: ")
        estudiante2_hobbies = input("Ingrese nuevos hobbies: ")
        estudiante2_fecha = verificar_y_corregir_fecha()
        
    elif(usuario_logueado == estudiante3_email):
        global estudiante3_nombre
        global estudiante3_biografia
        global estudiante3_hobbies
        global estudiante3_fecha
        
        estudiante3_nombre = input("Ingrese nuevo nombre: ")
        estudiante3_biografia = input("Ingrese nueva biografia: ")
        estudiante3_hobbies = input("Ingrese nuevos hobbies: ")
        estudiante3_fecha = verificar_y_corregir_fecha()

#Muestra el menu principal
def mostrar_menu():
    print("####MENU PRINCIPAL####")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("0. Salir")

#Muestra el submenu correspondiente a la opcion seleccionada
def mostrar_submenu():
    opcion_submenu = 'z'
    while opcion_submenu != 'c':
        match opcion_menu:
            case 1:
                print("1. Gestionar mi perfil")
                print("a. Editar mis datos personales")
                if(opcion_submenu == 'a'):
                    editar_datos()
                print("b. Eliminar mi perfil")
                if(opcion_submenu == 'b'):
                    cartel(1)
                print("c. Volver")
            case 2:
                print("2. Gestionar mi perfil")
                print("a. Ver candidatos")
                if(opcion_submenu == 'a'):
                    mostrar_candidatos()
                print("b. Reportar un candidato")
                if(opcion_submenu == 'b'):
                    cartel(1)
                print("c. Volver")
            case 3:
                print("3. Matcheos")
                print("a. Ver matcheos")
                if(opcion_submenu == 'a'):
                    cartel(1)
                print("b. Eliminar un matcheo")
                if(opcion_submenu == 'b'):
                    cartel(1)
                print("c. Volver")
            case 4:
                print("4. Reportes estadísticos")
                cartel(0)
                print("c. Volver")
        
        opcion_submenu = input("Ingrese una opcion: ")

#Muestra (En construccion). Recibe un parametro entero para determinar el espaciado inicial
def cartel(deep):
    match deep:
        case 0: 
            print("En construccion")
        case 1:
            print(" En construccion")
        case 2:
            print("  En construccion")
        
#Manejo login
while contador_login < 3:
    email = input("Ingrese un email: ")
    contraseña = getpass.getpass("Ingrese una contraseña: ")
    try:
        contraseña = int(contraseña)
    except:
        contador_login+=1
        print("La contraseña debe ser un numero entero.", "Reintentos restantes: ", (3-contador_login))
        continue
    
    if((email != estudiante1_email or contraseña != estudiante1_contraseña) 
        and (email != estudiante2_email or contraseña != estudiante2_contraseña) 
        and (email != estudiante3_email or contraseña != estudiante3_contraseña)):
        contador_login+=1
        print("Usuario y contraseña incorrectos.", "Reintentos restantes: ", (3-contador_login))
    else:
        print("Loguado con exito con el usuario: ", email),
        usuario_logueado = email
        break;

if(contador_login == 3):
    print("Se ha excedido el numero de intentos.")
    sys.exit()

while opcion_menu != 0:
    if(usuario_logueado):
        mostrar_menu()
        
        try:
            opcion_menu = int(input("Ingrese una opcion: "))
        except:
            print("Debe ingresar un numero")
            continue
        
        if(opcion_menu in [1, 2 ,3 ,4]):
            mostrar_submenu()

if(opcion_menu == 0):
    print("Saliendo..")