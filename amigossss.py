
import json
amigos={}
amigos['amigosList']=[]
amigos['amigosList'].append({'nombreAmigo':'Luis', 'apellidoAmigo': 'Sanchez', 'uniAmigo': 'TU Berlin','Hindex': '3'})
amigos['amigosList'].append({'nombreAmigo':'Juan', 'apellidoAmigo': 'Lopez', 'uniAmigo': 'Viadrina','Hindex': '13'})
amigos['amigosList'].append({'nombreAmigo':'Jose', 'apellidoAmigo': 'Martinez', 'uniAmigo': 'BTU','Hindex': '5'})
amigos['amigosList'].append({'nombreAmigo':'Galo', 'apellidoAmigo': 'Perez', 'uniAmigo': 'UFZ','Hindex': '18'})
friends=open('amigos.json', 'w')
json.dump(amigos,friends, indent=4)
