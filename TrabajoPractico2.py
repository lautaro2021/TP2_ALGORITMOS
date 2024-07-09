import os 
from getpass import getpass

estudiantes = [
    ["0","pepe@gmail.com","123", "i"],
    ["1","pedro@gmail.com","321", "a"],
    ["2","adri@gmail.com","123", "a"],
    ["3","lauti@gmail.com","123", "a"],
    ["","", "", ""],
    ["","", "", ""],
    ["","", "", ""],
    ["","", "", ""]
    ]
moderador =[
    ["0","lau@gmail.com","123", "a"],
    ["1","","", ""],
    ["2","","", ""],
    ["3","","", ""]
    ]

ultima_posicion_estudiantes = 4
ultima_posicion_moderadores = 1

usuario_logeado = ["",""]
#GENERAMOS LA VARIABLE INTENTO <= 3 PARA QUE NO HAYA ERROR
intento_login = 0

###FUNCIONES DE VALIDACION DE DATOS###
def fn_validar_si_numero(dato):
    try:
        int(dato)
        return True
    except ValueError:
        return False

def fn_validar_rango(inicio:int,limite:int):
    try:
        numero =int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("\nError, ingrese nuevamente el número\n")
            numero =int(input("Ingrese una opción: "))
        return numero
    except ValueError:
        print("\nError: Solamente se permiten numeros\n")
        return fn_validar_rango(inicio,limite)

def fn_validar_rango_mod_str():
    opc = input("Ingrese una opcion:")
    
    if(opc == 'a' or opc == 'b'):
        return opc
    else:
        print("\nError, ingrese opcion nuevamente")
        fn_validar_rango_mod_str()

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

def pr_cartel_construccion():
    print("\nOpcion en construccion...\n")
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
        email = input("\nIngrese el email: ")
        contrasena = getpass("\nIngrese una contraseña: ")

        desactivado = False
    
        if not(autenticado):
            # FUNCION INTERNA PARA BUSCAR USUARIOS EN EL ARRAY DE ESTUDIANTES
            def fn_busqueda_usuario(indice): 
                if(estudiantes[indice][1] ==email  and estudiantes[indice][2]==contrasena):
                    usuario_logeado[0] = email
                    usuario_logeado[1] = "U"

                    return True

            #BUSCAR USUARIO EN LA LISTA DE ESTUDIANTES
            res = fn_busqueda_secuencial_uni(8 ,fn_busqueda_usuario)
            encontrado, pos = res[0], res[1]
            
            if(encontrado):
                if estudiantes[pos][3] == 'a':
                    autenticado = True
                else:
                    desactivado = True
                    print("\nEl usuario se encuentra desactivado.\n")
            

        if not(autenticado):
            #FUNCION INTERNA PARA BUSCAR MODERADORES EN EL ARRAY DE MODERADORES
            def fn_busquedaModerador(indice):
                if moderador[indice][1] == email and moderador[indice][2] == contrasena:
                    usuario_logeado[0] = email
                    usuario_logeado[1] = "M"

                    return True

            #BUSCAR USUARIO EN LA LISTA DE MODERADORES
            res = fn_busqueda_secuencial_uni(4,fn_busquedaModerador)
            encontrado, pos = res[0], res[1]

            if(encontrado):
                if moderador[pos][3] == 'a':
                    autenticado = True
                else:
                    desactivado = True
                    print("\nEl usuario se encuentra desactivado.\n")

        if not desactivado:
            print("\nUsuario o contrasena incorrectos. Intente nuevamente")
        
        intento_login = intento_login + 1
            
        print(f"Numero de intentos restantes: {3 - intento_login}")

    #SI EL AUTENTICADO ES TRUE ENTONCES SE TE DIRIGE AL MENU PRINCIPAL Y SI NO SALE DEL PROGRAMA 
    if(autenticado):
        intento_login = 0
        if usuario_logeado[1]=="U":
            autenticado = fn_menu_usr()
        elif usuario_logeado[1]=="M":
            autenticado = fn_menu_mod()

    return autenticado

def fn_desactivar_usuario():
    pr_limpiar_consola()
    pr_crear_titulo("DESACTIVAR USUARIO")
    
    desactivado = False
    while not desactivado:
        pos = 100
        encontrado = False
        
        opc = input("\nIngrese un usuario o ID: ")
        try:
            opc = int(opc)
            
            def fn_desactivar_usu_por_id(indice):
                if estudiantes[indice][0] == str(opc):
                    return True
            
            encontrado = fn_busqueda_secuencial_uni(8, fn_desactivar_usu_por_id)[0]
            pos = fn_busqueda_secuencial_uni(8, fn_desactivar_usu_por_id)[1]
                
        except ValueError:
            def fn_buscar_usu_por_email(indice):
                if estudiantes[indice][1] == opc:
                    return True
                               
            encontrado = fn_busqueda_secuencial_uni(8, fn_buscar_usu_por_email)[0]
            pos = fn_busqueda_secuencial_uni(8, fn_buscar_usu_por_email)[1]
        
        if not encontrado:
            print("\nUsuario no encontrado. Intente nuevamente.\n")

        else:
            print(f"\nEsta seguro que desea desactivar al usuario: {estudiantes[pos][1]} ?\n\n1-Si\n\n2-No\n")
            confirm = fn_validar_rango(1, 2)
            if confirm == 1:
                if estudiantes[pos][3] == 'a':
                    estudiantes[pos][3] = 'i'
                    print('\nUsuario desactivado con exito.\n')
                    desactivado = True
                else:
                    desactivado = True
                    print("\nEl usuario ya se encuentra desactivado.\n")
            
            else:
                desactivado = True
                
    return desactivado

def fn_gestionar_usuarios():
    pr_limpiar_consola()
    pr_crear_titulo("GESTIONAR USUARIOS")
    
    band = True
    while band:
        print("\na.Desactivar usuario\n\nb-Volver\n\n")
        opc = fn_validar_rango_mod_str()
        
        match opc:
            case 'a':
                fn_desactivar_usuario()
            case 'b':
                pr_limpiar_consola()
                pr_crear_titulo("MENU PRINCIPAL")
                band = False
        
    return band
        
def fn_menu_mod():
    pr_limpiar_consola()
    pr_crear_titulo("MENU PRINCIPAL")
    band= True
    while band:
        print("\n1.Gestionar usuarios\n\n2-Gestionar reportes\n\n3-Reportes estadisticos\n\n4-salir\n\n")
        opc = fn_validar_rango(1, 4)
        
        match opc:
            case 1:
                 fn_gestionar_usuarios()
            case 2:
                 print("gestionarreportes()")
            case 3:
                 pr_cartel_construccion()
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
            pr_limpiar_consola()
            print('\nSe ha quedado sin intentos.')
            opc = 0
        else:
             opc = fn_validar_rango(0, 2)
    
    print("\nSaliendo del programa.\n")

inicializacion()