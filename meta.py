from __future__ import division
from PIL import Image
from PIL.ExifTags import TAGS
from os import listdir
from os.path import isfile, join
import csv
from os import path

radio = 6366000     #metros
global csvFile
csvFile = open('./csvFile.csv', mode='w')
global writ
writ = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writ.writerow(['fileName', 'Latitude', 'Longitude', 'Altitude'])



onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
for file in onlyfiles:
    #print(file)
    if file[len(file) -1] != 'y' and file[len(file) -1] != 'v':
        imagen = Image.open(file)
        # Obtener metadatos
        datos_exif = imagen.getexif()
 
        # Diccionario en el cual se guardaran los datos
        exif_dic = {}
 
        # Ciclo para decodificar los datos
        for tag, value in datos_exif.items():
            # Obtener el nombre de la etiqueta etiqueta
            etiqueta = TAGS.get(tag, tag)
    
            if etiqueta == 'GPSInfo':
                #global writ
                print(file, '   ', etiqueta)
                valor = datos_exif.get(tag)
                
                

                lat = valor[2]
                #print(valor[2][0], ' ', valor[2][1]*2)
                decimalLat = valor[2][0] + valor[2][1]/60 + valor[2][2]/3600
                lng = valor[4]
                decimalLong = valor[4][0] + valor[4][1]/60 + valor[4][2]/3600
                alt = valor[6]
                writ.writerow([file,float(decimalLat),float(decimalLong),alt])



                
                print(etiqueta, ': Latitude:', float(decimalLat) , ' Longitude:', float(decimalLong), ' Altitude: ', alt)

 
# Obtener metadatos
"""datos_exif = imagen.getexif()
 
# Diccionario en el cual se guardaran los datos
exif_dic = {}
 
# Ciclo para decodificar los datos
for tag, value in datos_exif.items():
    # Obtener el nombre de la etiqueta etiqueta
    etiqueta = TAGS.get(tag, tag)
    
    if etiqueta == 'GPSInfo':
        print(etiqueta)
        valor = datos_exif.get(tag)
        print(valor)        
        lat = valor[2]
        lng = valor[4]
        alt = valor[6]
        print(lat , ' ', lng)


    # Obtener el valor de la etiqueta
    #valor = datos_exif.get(tag)
    #exif_dic[etiqueta] = valor
    # Imprimir los datos
    #print(str(etiqueta) + " : " +str(valor))


# Leer imagen
"""
