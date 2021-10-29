#Esta red social está enfocada en la comunidad de académica.
#El propósito es meramente académico. Los objetivos son:
#Permitir compartir avances investigativos importantes.
#Mantenerse en contacto con investigadores en su tema de interes.
#Permitir el contacto basico entre investigadores seniors y principiantes.
#Aumentar el networking, especialmente para personas que acaban de demostrar interes en el campo academico.
#Facilitar la innovación y colaboraciones entre académicos
#Se pueden generar debates meramente acádemicos

usuario=''
estado=''
mensaje=''


import funciones as red
import os
import sys
import json

red.bienvenida()
usuario=red.userPerfil()
print('Hola', str(usuario), 'Bienvenido a Forschnet!')


#VERIFICACION
if red.archivo_existente(usuario+'.user'):
    print('Leyendo datos de usuario ', usuario, 'desde su perfil.')
    (usuario, edad, email,hindex,  institut, pais, amigos,estado, wall)= red.leer_user(usuario)
else:
    edad=red.get_age()
    email = red.askCorreo()
    hindex = red.get_hindex()
    institut=red.get_institut()
    pais=red.get_pais()
    amigos=red.get_amigos()
    estado='Hola mundo!'
    wall=[]


print('Hola ', str(usuario), 'Estamos felices de tenerte en Forschnet!')
print('Registro exitoso.\n Sesion Iniciada')

print('*'*30)
print('Este es tu perfil: ')
red.perfil(usuario, edad, email,hindex, institut, pais, amigos)
red.display(usuario, estado)

#ACTIVIDADES
import re
actividad=1
while actividad!=0:
    actividad = red.actividades()
    try:
        if actividad == 1:
            estado=red.type_message()
            red.invest(usuario,amigos, estado, wall)

        elif actividad == 2:
            estado= red.type_message()
            red.jobad(usuario, amigos, estado, wall)

        elif actividad == 3:
            estado=red.type_message()
            red.personal(usuario, amigos, estado, wall)

        elif actividad == 4:
            estado=red.type_message() #revisar en estos con publicar y obtener mensaje
            red.privat(usuario, amigos, estado, wall)

        elif actividad == 5:
            usuario = red.userPerfil()
            edad = red.get_age()
            email = red.askCorreo()
            hindex = red.get_hindex()
            institut = red.get_institut()
            pais = red.get_pais()
            amigos = red.get_amigos()
            print('Gracias por actualizar los datos.')

        elif actividad == 6:
            red.amigoslista1()

        elif actividad ==7:
            red.display_wall(wall)

        elif actividad == 0:
            print('Usted ha decidido salir. Sus datos de perfil se guardarán como: ',usuario+'.user')
            red.write_user(usuario,edad,email,hindex, institut, pais, amigos,estado, wall)
            print('Su perfil: ', usuario+'.user', 'se ha guardado exitosamente!')
            break
    except ValueError:
            print('Carácter invalido, ingrese un numero.')
            actividad=red.actividades()
print('Gracias por usar Forschnet!')
red.logout()

''''
import json
amigos={}
amigos['amigosList']=[]
amigos['amigosList'].append({'nombreAmigo':'Luis', 'apellidoAmigo': 'Sanchez', 'uniAmigo': 'TU Berlin','Hindex': '3'})
amigos['amigosList'].append({'nombreAmigo':'Juan', 'apellidoAmigo': 'Lopez', 'uniAmigo': 'Viadrina','Hindex': '13'})
amigos['amigosList'].append({'nombreAmigo':'Jose', 'apellidoAmigo': 'Martinez', 'uniAmigo': 'BTU','Hindex': '5'})
amigos['amigosList'].append({'nombreAmigo':'Galo', 'apellidoAmigo': 'Perez', 'uniAmigo': 'UFZ','Hindex': '18'})
friends=open('amigos.json', 'w')
json.dump(amigos,friends, indent=4)
'''










