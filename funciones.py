
import os

def bienvenida():
    print('''
    ##d88888b  .d88b.  d8888b. .d8888.  .o88b. db   db d8b   db d88888b d888888b
      88'     .8P  Y8. 88  `8D 88'  YP d8P  Y8 88   88 888o  88 88'     `~~88~~'
      88ooo   88    88 88oobY' `8bo.   8P      88ooo88 88V8o 88 88ooooo    88
      88~~~   88    88 88`8b     `Y8b. 8b      88~~~88 88 V8o88 88~~~~~    88
      88      `8b  d8' 88 `88. db   8D Y8b  d8 88   88 88  V888 88.        88
      YP       `Y88P'  88   YD `8888Y'  `Y88P' YP   YP VP   V8P Y88888P    YP  ''')

    print('Bienvenido a Forschnet')
    print('+'*55)
    print('Inicie Sesion o Registrese ')
    print('+'*55)

def userPerfil():
    usuario=str(input('Ingrese su nombre de usuario: '))
    return usuario

def get_age():
    while True:
        try:
            anio = int(input('Para empezar con tu perfil académico, nos gustaría saber tu ano de nacimiento:'))
            break
        except ValueError:
            print('Por favor digite un numero.')
    edad=2021-anio-1
    return edad

def askCorreo():
    import re
    arroba='@'
    email = input('Ingresa tu correo electronico academico: ')
    if re.search(arroba, email):
        print('correo válido')
    else:
        print('invalid email')
        email = input('Ingresa tu correo electronico academico: ')
    return email

def get_institut():
    institut=input('Ingrese el nombre de su Universidad o Instituto: ')
    return institut

def get_pais():
    pais=input('Indica tu país: ')
    return pais
         
def get_hindex():
    while True:
        try:
            hindex = int(input('Cuentanos cuentános acerca de su número de H-index:  '))
            if hindex <= 3:
                print('Nos alegra que quieras iniciar tu camino en la investigación con nosotros. Buena suerte y recuerda que el '
          'cielo es el límite.')
            elif hindex > 3 < 15:
                print('Wow! Eres muy talentoso. Por favor, sigue aportando al mundo tus conocimientos.')
            elif hindex >= 16:
                print('Eres alguien digno de admirar. Has hecho grandes aportes a la investigación. Muchas personas creen en ti y'
          'seguro quieres que muchas mas sigan tu camino. Que estés aquí nos hace sentir honrados. Gracias por querer '
          'aportar más en tu campo de investigación.')
            break
        except ValueError:
            print('Oppss! Al parecer hay un error en los datos que ingresaste.')
    return hindex

def get_amigos():
    amigo=input('Ingrese el nombre de sus amigos separados por comas(,): ')
    amigos=amigo.split(',')
    return amigos

def get_data():
    n=newUser()
    a=askCorreo()
    h=get_hindex()
    i=get_institut()
    p=get_pais()
    f=get_amigos()
    return(n,a,h,i,p,f)


def perfil(usuario, edad, email,hindex, institut, pais, amigos):
    print('*'*30)
    print('Nombre: '+usuario)
    print('Edad: ', edad, 'anios')
    print('email:', email)
    print('H-Index: ', hindex)
    print('Instituto/Universidad: ', institut)
    print('País: ', pais)
    print('Número de amigos: ', len(amigos))
    print('*'*55)

def actividades():
    print('*******************************************************')
    print('Que desea hacer ahora?:')
    print('1. Para escribir un anuncio acerca de su actual investigación.')
    print('2. Para publicar una oferta de trabajo personal en su actual/futura investigación.')
    print('3. Para publicar mensaje personal. ')
    print('4. Contactar un amigo/colega/estudiante para una propuesta de investigación.')
    print('5. Actualizar su perfil.')
    print('6. Para ver lista de amigos.')
    print('7. Para ver el muro. ')
    print('0. Para salir.')
    while True:
        try:
            actividad = int(input('Ingrese la opción deseada: '))
            while actividad < 0 or actividad > 7:
                print('Opción incorrecta. Intente ingresando una de las opciones del menú.')
                actividad=int(input('Ingrese la opción deseada: '))
            break
        except ValueError:
            print('No es valido. Ingrese un numero')
    return actividad
        
def type_message():
    mensaje=input('Escriba aquí su mensaje: ')
    return mensaje

def invest(usuario, amigos, mensaje, wall):
    print('*******************************')
    print(usuario,'Desea hacer un anuncio acerca de su investigación. Para tus amigos, estudiantes'
                    ' y colegas podría ser muy interesante. Por favor vea su anuncio aqui: ', mensaje)
    print('*******************************')
    wall.append(mensaje)
    for amigo in amigos:
        if archivo_existente(amigo + '.user'):
            fileus = open(amigo + '.user', 'a')
            fileus.write(usuario + ':' + mensaje + '\n')
            fileus.close

def jobad(usuario,amigos, mensaje, wall):
    print('*******************************')
    print(usuario, 'Tiene la siguiente propuesta de trabajo, pasantía o colaboración: ', mensaje)
    print('*******************************')
    wall.append(mensaje)
    for amigo in amigos:
        if archivo_existente(amigo + '.user'):
            fileus = open(amigo + '.user', 'a')
            fileus.write(usuario + ':' + mensaje + '\n')
            fileus.close

def personal(usuario, amigos, mensaje, wall):
    print('*******************************')
    print(usuario, 'comparte el siguiente mensaje: ', mensaje)
    print('*******************************')
    wall.append(mensaje)
    for amigo in amigos:
        if archivo_existente(amigo + '.user'):
            fileus = open(amigo + '.user', 'a')
            fileus.write(usuario + ':' + mensaje + '\n')
            fileus.close

def privat(usuario, amigos,  mensaje, wall):#publicar diferenciarlo de obtener
    print('*******************************')
    print('Querid@ usuario, el usuario',usuario, 'te ha enviado el siguiente mensaje privado:, ', mensaje)
    print('*******************************')
    wall.append(mensaje)
    for amigo in amigos:
        if archivo_existente(amigo + '.user'):
            fileus = open(amigo + '.user', 'a')
            fileus.write(usuario + ':' + mensaje + '\n')
            fileus.close

def display(usuario, estado):
    print('+'*40)
    print(usuario +':', estado)
    print('+' * 40)
    return estado

def leer_mensaje(usuario, mensaje):
    print('*' * 30)
    print(usuario+':', mensaje)
    print('*' * 30)

def display_wall(wall):
    print('+++++++++++WALL++++++++++('+str(len(wall))+'mensajes)+++++++++++++++++++')
    for mensaje in wall:
        print(mensaje)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    
def timeline(usuario,amigos,mensaje, wall):
    print('*' * 30)
    print(origen, 'dice: ' ,mensaje)
    print('*' * 30)
    wall.append(mensaje)
    

def leer_user(usuario):
    file_user = open(usuario + '.user', 'r')
    usuario = file_user.readline().rstrip()
    edad = int(file_user.readline())
    email = file_user.readline().rstrip()
    hindex = file_user.readline().rstrip()
    institut = file_user.readline().rstrip()
    pais = file_user.readline().rstrip()
    amigos = file_user.readline().rstrip().split(',')
    estado=file_user.readline().rstrip()
    #n_contacts son los amigos.
    wall = []
    mensaje =file_user.readline().rstrip()
    while mensaje != "":
        wall.append(mensaje)
        mensaje = file_user.readline().rstrip()
    file_user.close()
    return(usuario, edad, hindex, email, institut, pais, amigos, estado, wall)

def write_user(usuario, edad,email,hindex, institut, pais, amigos,estado, wall):
    file_user=open(str(usuario)+'.user', 'w')
    file_user.write(usuario)
    file_user.write('\n')
    file_user.write(str(edad)+ "\n")
    file_user.write(str(email)+ '\n')
    file_user.write(str(hindex)+ "\n")
    file_user.write(institut+"\n")
    file_user.write(pais + '\n')
    file_user.write(",".join(amigos) + "\n")
    file_user.write(estado + "\n")
    for mensaje in wall:
        file_user.write(mensaje+'\n')
    file_user.close()

def archivo_existente(ruta):
    import os.path
    return os.path.isfile(ruta)

def amigoslista1():
    import json
    with open('amigos.json') as friends:
        amigos = json.load(friends) 
        for amigo in amigos["amigosList"]:
            print('Nombre:', amigo['nombreAmigo'])
            print('Apellido: ', amigo['apellidoAmigo'])
            print('Institucion/Universidad: ', amigo['uniAmigo'])
            print('H-index: ', amigo['Hindex'])
            print('')

def nombrefile(usuario):
    usuario.replace('\n', '')


def logout():
    print('''
     ( 

                    .   ,- Nos vemos pronto !
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )

               ____
          .-'""p 8o""`-.
       .-'8888P'Y.`Y[ ' `-.
     ,']88888b.J8oo_      '`.
   ,' ,88888888888["        Y`.
  /   8888888888P            Y8\
 /    Y8888888P'             ]88\
:     `Y88'   P              `888:
:       Y8.oP '- >            Y88:
|          `Yb  __             `'|
:            `'d8888bo.          :
:             d88888888ooo.      ;
 \            Y88888888888P     /
  \            `Y88888888P     /
   `.            d88888P'    ,'
     `.          888PP'    ,'
       `-.      d8P'    ,-'   -Forschnet-
          `-.,,_'__,,.-''
''')


def validar_paquete():
    import os
    return os


#cerrarjsonn
#nombre.close()