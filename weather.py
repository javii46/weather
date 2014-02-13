#encoding=utf-8
import json
import requests
print 'Lista de las ciudades.' """

1. Almeria
2. Cadiz
3. Cordoba
4. Granada
5. Huelva
6. Jaen
7. Malaga
8. Sevilla

"""

diccionario = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}

consulta = raw_input("Introduce el número de la ciudad para saber su temperatura: ")
prov=diccionario[consulta]
respuesta=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,%s' % (prov, "spain")})
dicc=json.loads(respuesta.text)
temperatura=dicc["main"]["temp"] 
gradoscentigrados=temperatura - 273
print "La temperatura de",prov,"es",gradoscentigrados,"grados centígrados."
