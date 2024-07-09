import os 
from getpass import getpass

estudiantes = [
    ["0","pepe@gmail.com","123", "a"],
    ["1","pedro@gmail.com","321", "a"],
    ["2","adri@gmail.com","123", "a"],
    ["3","lauti@gmail.com","123", "a"],
    ["","", "", ""],
    ["","", "", ""],
    ["","", "", ""],
    ["","", "", ""]
    ] # FALTA CARGAR LOS 0TROS 4
moderador =[
    ["0","alejo@gmail.com","123", "a"],
    ["1","","", ""],
    ["2","","", ""],
    ["3","","", ""]
    ]

usuario_logeado = ["",""]
#GENERAMOS LA VARIABLE INTENTO <= 3 PARA QUE NO HAYA ERROR
intento_login = 0

ultima_posicion_estudiantes = 4
ultima_posicion_moderadores = 1

###FUNCIONES DE VALIDACION DE DATOS###
def fn_validar_si_numero(dato):
    try:
        int(dato)
        return True
    except ValueError:
        return False

def fn_validar_rango(inicio:int,limite:int):
    try:
        numero =int(input(f"Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("\nError, ingrese nuevamente el número\n")
            numero =int(input(f"Ingrese una opción: "))
        return numero
    except ValueError:
        print("\nError: Solamente se permiten numeros\n")
        return fn_validar_rango(inicio,limite)

###PROCEDIMIENTOS###
def pr_mostrar_opcion_invalida():
    print("Opción o formato no válido. Por favor, intente de nuevo.")

def pr_mostrar_usuario_inexistente():
    print("Usuario inexistente. Por favor, intente de nuevo.")

def pr_crear_titulo(titulo:str):
    columnas="" 
    
    cantidadLetra:int = len(titulo) # ES LA CANTIDAD DE LETRAS QUE TIENE EL TITULO
    columnaTamano:int = os.get_terminal_size().columns

    for i in range(0,columnaTamano):
        columnas= columnas + "_"
    
    copiarColumnas = (columnaTamano - cantidadLetra )//2

    print(columnas)
    print("\n" + " " * copiarColumnas + titulo )
    print(columnas)
    
def pr_limpiar_consola():
    os.system("cls")
###FUNCIONES GENERALES###
def fn_busqueda_secuencial_uni(limite:int,condicion) -> bool:
    encontrado = False
    index = 0
    while  index <  limite and not(encontrado):
        encontrado = condicion(index)
        index = index + 1 
        
    return [encontrado, index - 1]

###FUNCIONES PRINCIPALES###
def fn_editar_datos(indice):
    pr_crear_titulo("Editar mi perfil")

    def fn_buscar_usuario_correspondiente(Index1):
        if(estudiantes[Index1][0] == usuario_logeado[0]):
            return True
    
    usuario= fn_busqueda_secuencial_uni(8, fn_buscar_usuario_correspondiente)[1]
    
    estudiantes[usuario][indice]=str(input("ingrese la nueva bios: "))
    print(estudiantes)

def fn_registrar_moderadores():
    global ultima_posicion_moderadores
    creado_exitoso = False
    
    if ultima_posicion_moderadores == 4:
        print("\nNo es posible registrar mas estudiantes. Limite máximo alcanzado.\n")
        return creado_exitoso
    
    pr_limpiar_consola()
    pr_crear_titulo("Registrarse")
    
    email = input("Ingrese email: ")
    password = getpass("Ingrese una contraseña: ")

    estudiantes[ultima_posicion_moderadores][0] = str(ultima_posicion_moderadores)
    estudiantes[ultima_posicion_moderadores][1] = email
    estudiantes[ultima_posicion_moderadores][2] = password
    estudiantes[ultima_posicion_moderadores][3] = 'a'
    
    ultima_posicion_moderadores+=1
    
    creado_exitoso = True
 
    return creado_exitoso

def fn_registrar_estudiante():
    global ultima_posicion_estudiantes
    creado_exitoso = False
    
    if ultima_posicion_estudiantes == 8:
        print("\nNo es posible registrar mas estudiantes. Limite máximo alcanzado.\n")
        print(estudiantes)
        return creado_exitoso
    
    pr_limpiar_consola()
    pr_crear_titulo("Registrarse")
    
    email = input("Ingrese email: ")
    password = getpass("Ingrese una contraseña: ")
    estudiantes[ultima_posicion_estudiantes][0] = str(ultima_posicion_estudiantes)
    estudiantes[ultima_posicion_estudiantes][1] = email
    estudiantes[ultima_posicion_estudiantes][2] = password
    estudiantes[ultima_posicion_estudiantes][3] = 'a'
    
    ultima_posicion_estudiantes+=1

    creado_exitoso = True
 
    return creado_exitoso

def fn_iniciar_sesion():
    global intento_login
    
    pr_limpiar_consola()
    pr_crear_titulo("Loguearse")
    
    #LA VARIABLE AUTENTICADO SIRVE COMO BOOLEANO PARA SABER CUANDO EL USUARIO ESTA LOGEADO
    autenticado = False
  
    while intento_login < 3 and not(autenticado): 
        email = input("Ingrese el email: ")
        contrasena = getpass("Ingrese una contraseña: ")

        if not(autenticado):
            # FUNCION INTERNA PARA BUSCAR USUARIOS EN EL ARRAY DE ESTUDIANTES
            def fn_busqueda_usuario(indice): 
                if(estudiantes[indice][1] ==email  and estudiantes[indice][2]==contrasena):
                    usuario_logeado[0] = email
                    usuario_logeado[1] = "U"

                    return True

            #BUSCAR USUARIO EN LA LISTA DE ESTUDIANTES
            autenticado = fn_busqueda_secuencial_uni(8, fn_busqueda_usuario)[0]

        if not(autenticado):
            #FUNCION INTERNA PARA BUSCAR MODERADORES EN EL ARRAY DE MODERADORES
            def fn_busquedaModerador(indice):
                if moderador[indice][1] == email and moderador[indice][2] == contrasena:
                    usuario_logeado[0] = email
                    usuario_logeado[1] = "M"

                    return True

            #BUSCAR USUARIO EN LA LISTA DE MODERADORES
            autenticado = fn_busqueda_secuencial_uni(4,fn_busquedaModerador)[0]
        
        if not(autenticado):
            print("\nEl email o la contrasena son incorrectas"),
            
        intento_login = intento_login + 1
        
        if 3 - intento_login == 0:
            print("Se ha quedado sin intentos. Saliendo del programa.")
        else:
            print(f"Numero de intentos restantes: {3 - intento_login}")

    #SI EL AUTENTICADO ES TRUE ENTONCES SE TE DIRIGE AL MENU PRINCIPAL Y SI NO SALE DEL PROGRAMA 
    if(autenticado):
        if usuario_logeado[1]=="U":
            autenticado = fn_menu_usr()
        elif usuario_logeado[1]=="M":
            autenticado = fn_menu_mod()
        #MenuPrincipal()

    return autenticado
    
def fn_menu_mod():
    pr_limpiar_consola()
    pr_crear_titulo("MENU PRINCIPAL")
    band= True
    while band:
        print("1.Gestionar usuarios\n2-Gestionar reportes\n3-Reportes estadisticos\n4-salir")
        opc = fn_validar_rango(1, 4)
        
        match opc:
            case 1:
                 print("Gestionarusuarios()")
            case 2:
                 print("gestionarreportes()")
            case 3:
                 print("reportesestadisticos()")
            case 4:
                band=False
    
    return band

def fn_menu_usr():
    pr_limpiar_consola()
    pr_crear_titulo("Menu Principal")
    
    band=True
    while band:
        print("\n1.Gestionar mi perfil\n\n2-Ver candidatos\n\n3-Ver matcheos\n\n4-Reportes estadisticos\n\n5-Salir\n")
        print("\nIngrese el numero correspondiente a la opcion que desea ingresar" )
        print("")
        opc = fn_validar_rango(0,5)
        if opc== 1:
            fn_editar_datos(usuario_logeado[0],2)
        elif opc == 2:
            print("#ver candidatios()")
        elif opc == 3:
            print("En construccion...")
        elif opc == 5:
            band=False
            
    return band

def inicializacion():
    global intento_login
        
    pr_limpiar_consola()
    pr_crear_titulo("Bienvenido, ¿buscando al compañero ideal?  ")
    print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
    
    opc = fn_validar_rango(0, 2)
    while opc != 0:
        if(opc == 1):
            if not fn_iniciar_sesion():
                pr_limpiar_consola()
                pr_crear_titulo("Bienvenido, ¿buscando al compañero ideal?  ")
                print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
        elif (opc == 2):
            if fn_registrar_estudiante():
                pr_crear_titulo("Cuenta creada con exito")
                print("\n1-Iniciar sesion\n\n2-Registrarse\n\n0-Salir\n\n")
        if(intento_login == 3):
            opc = 0
        else:
             opc = fn_validar_rango(0, 2)
    
    print("\nSaliendo del programa.\n")

inicializacion()