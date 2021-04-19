# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:23:35 2021

@author: Sergi
"""

#En primer lugar se importan los módulos a utilizar. 

from openpyxl import Workbook
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import scipy.stats as scpstats

#A continuación se leen los csv haciendo uso de pandas.

gravim_data = pd.read_csv("filtros_hvs_20_4_10-intervalo_20200601-20201231_SCO_.csv", header=0, sep = ", ", engine = "python", )

beta_data = pd.read_csv("202006_202012_Beta_Raw_Data.csv", header=0)

meteo_data = pd.read_csv("202006_202012_Meteo_SCO.csv", header=0)

Junio = pd.read_csv("Junio_2020.csv", header=0, sep = ",", engine = "python", )

Julio = pd.read_csv("Julio_2020.csv", header=0, sep = ",", engine = "python", )

Agosto = pd.read_csv("Agosto_2020.csv", header=0, sep = ",", engine = "python", )

Septiembre = pd.read_csv("Septiembre_2020.csv", header=0, sep = ",", engine = "python", )

Noviembre = pd.read_csv("Noviembre_2020.csv", header=0, sep = ",", engine = "python", )

Diciembre = pd.read_csv("Diciembre_2020.csv", header=0, sep = ",", engine = "python", )

#Ahora concateno todos los datframes de meses de medidas de redes de calidad del gobierno para tener un único dataframe
#Con todas las medidas de las redes de calibración, y las mismas columnas para todos ellos, pues tienen los mismo nombres,
#lo único que hace es añadir nuevas filas, no columnas.

concat=pd.concat([Junio, Julio, Agosto, Septiembre, Noviembre, Diciembre])


#Muchas de las medidas son erroneas, por eso necesito limpiar las que tienen flags que no sean "V", que indican que la medida
#Ha sido válida. Para ello, creo una mask que me filtre solo los valores de flag en tome cano y parque la granja igual a "V"

flag_tome = concat["Flag_Tome"]                         #Saco las columnas de flag como variables
flag_granja = concat["Flag_Granja"]
mask_meses = (flag_tome == "V")&(flag_granja == "V")    #Creo la mask para coger solo valores validos de flag
concat = concat[mask_meses]   #Filtro para tener solo valores verdaderos

#Ahora como siempre, convierto mis fechas a datetime

fechas_concat = concat["Fecha"]          
fechas_concat = pd.to_datetime(fechas_concat,dayfirst=True)
concat["Fecha"] = fechas_concat


inicio_gravim = gravim_data["Inicio muestreo"]  #Asigno dias de inicio de medida de gravimetrico a una variable
inicio_gravim = pd.to_datetime(inicio_gravim)   #Convierto esa variable a datetime
gravim_data["Inicio muestreo"] = inicio_gravim  #Vuelvo a meter los días de inicio en el dataframe ahora como datetimes

#Suprimo también el logbook aplicando una mask

timestampx = beta_data["timestampx"]
mask = (timestampx>'2020-06-01 00:00:00')&(timestampx<'2020-07-15 00:00:00')|(timestampx>'2020-07-15 18:00:00')&(timestampx<'2020-07-20 09:00:00')|(timestampx>'2020-07-20 18:00:00')&(timestampx<'2020-08-31 00:00:00')|(timestampx>'2020-09-01 17:30:00')&(timestampx<'2020-11-27 14:00:00')|(timestampx>'2020-11-28 14:00:00')&(timestampx<'2021-01-01 00:00:00')
beta_data = beta_data[mask]  #Aplico la mask, que restringe los días del logbook

#Ahora no es necesario restar 8 horas, puedo simplemente pasar mis fechas a datetime.

fechas_beta = beta_data["timestampx"]           #Asigno fechas de medidas de beta a una variable
fechas_beta = pd.to_datetime(fechas_beta)       #Convierto a datetime
beta_data["timestampx"] = fechas_beta           #Meto los nuevos valores de fechas en el dataframe (ahora como datetimes)

#Creo de la misma manera que antes un nuevo dataframe que considere medidas en fechas iguales, si alguna fecha no tiene medidas, se quita.
#Esto lo hago así porque las redes indican las horas por separado, si relacionara horas no podría relacionar fechas.

merge2 = beta_data.merge(concat,left_on = beta_data["timestampx"].dt.date, right_on = concat["Fecha"].dt.date)

#Saco las fechas y horas de mis medidas de beta, para usarlas en el bucle

hours_beta = merge2["timestampx"].dt.hour
dates_beta= merge2["timestampx"].dt.date

#Asigno las columnas que me interesan a variables

pm_beta = merge2["pm"]
pm_tome = merge2["Tome Cano PM10 (µg/m³)"]
pm_granja = merge2["Parque La Granja-Sta Cruz de TF PM10 (µg/m³)"]


#Ahora calcularé las medias horarias de PM10 por mi atenuador, y luego las medias diarias por mi atenuador y los de red de calidad.

#Creo arrays vacíos para introducir los calculos

pm_gravim_no_repetidos = ([])   
medias_beta = ([])
desviaciones_beta = ([])            
desviaciones_beta_dia = ([])  
y_hour=([])                         
media_hora=([])    
desv_hora=([])       

media_hora_tome=([])
media_hora_granja=([])
medias_beta_tome=([])
medias_beta_granja=([])

#Creo un bucle muy similar a los ya usados, pero ahora calculo la media horaria de mi atenuador, y luego la media diaria
#tanto de mi atenuador como de los de redes de calidad, para comparar esos valores.

rango = (len(merge2))  #Rango de actuación del bucle

for j in range(rango):      
    if j == (rango-1):                              #Esto lo añado para evitar un error en el último término.
        y_hour.append(pm_beta[j])                           #Basicamente hago todo lo que se ha ido haciendo.
        medias_beta.append(np.mean(y_hour))
        medias_beta_tome.append(pm_tome[j])
        medias_beta_granja.append(pm_granja[j])
        desv_hora.append(np.std(y_hour))
        break 
     
    if hours_beta[j] == hours_beta[j+1]:          #Horas iguales
        y_hour.append(pm_beta[j])                    
        #continue
    
    if hours_beta[j] != hours_beta[j+1]:          #Cambio de hora
        medias_beta.append(np.mean(y_hour))
        medias_beta_tome.append(pm_tome[j])
        medias_beta_granja.append(pm_granja[j])
        desv_hora.append(np.std(y_hour))
        y_hour=([])
        
"""     
    if dates_beta[j] != dates_beta[j+1]:        #Cambio de día
        medias_beta.append(np.mean(media_hora))  
        medias_beta_tome.append(np.mean(media_hora_tome))        
        medias_beta_granja.append(np.mean(media_hora_granja))
        #desviaciones_beta.append(np.mean(desv_hora))
        #desviaciones_beta_dia.append(np.std(media_hora))    #desmarcando esto podría calcular también desviación estándar
        media_hora = ([])                                    #Reseteo los arrays
        desv_hora = ([])
        media_hora_tome=([])
        media_hora_granja=([])
    
        #continue
"""


#Ahora ya puedo hacer un ajuste lineal de mis datos, uno para Tome Cano y otro para la granja.

#Tome cano.

ajuste_tome = scpstats.linregress(medias_beta_tome,medias_beta)

#Calculo las medidas de "y" usando mi ajuste para representarlo graficamente.

y_ajuste_tome=([])
for i in  range(len(medias_beta_tome)):
    calculo = ajuste_tome[0]*medias_beta_tome[i] + ajuste_tome[1]
    y_ajuste_tome.append(calculo)

#Parque La Granja

ajuste_granja = scpstats.linregress(medias_beta_granja,medias_beta)

#Calculo las medidas de "y" usando mi ajuste para representarlo graficamente.
y_ajuste_granja=([])
for i in  range(len(medias_beta_granja)):
    calculo = ajuste_granja[0]*medias_beta_granja[i] + ajuste_granja[1]
    y_ajuste_granja.append(calculo)


#Y ahora ya represento mis resultados 


plt.figure()
plt.title(r"Comparación del PM10 medido por BAM en CIAI (Santa Cruz) y Tome Cano")
plt.plot(medias_beta_tome, medias_beta,".")
plt.plot(medias_beta_tome, y_ajuste_tome, label= "Ajuste ($a=%.3f, b=%.3f,r^2= %.3f $ )" %(ajuste_tome[0],ajuste_tome[1],ajuste_tome[2]))
plt.xlabel("PM10 medido en Tome Cano (red de calidad del gobierno) [$\mu g / m^3$]")
plt.xlim(0,125)
plt.ylim(0,125)
plt.ylabel(r"PM10 medido en CIAI (Santa Cruz) [$\mu g / m^3$]")
plt.legend()
plt.grid(linewidth=0.3)
plt.savefig("Comparacion_BAM_ciai_tome_cano.png")

plt.figure()
plt.title(r"Comparación del PM10 medido por BAM en CIAI (Santa Cruz) y parque La Granja")
plt.plot(medias_beta_granja, medias_beta,".")
plt.plot(medias_beta_granja, y_ajuste_granja, label= "Ajuste ($a=%.3f, b=%.3f,r^2= %.3f $ )" %(ajuste_granja[0],ajuste_granja[1],ajuste_granja[2]))
plt.xlabel("PM10 medido en parque La Granja (red de calidad del gobierno) [$\mu g / m^3$]")
plt.xlim(0,150)
plt.ylim(0,150)
plt.ylabel(r"PM10 medido en CIAI (Santa Cruz) [$\mu g / m^3$]")
plt.legend()
plt.grid(linewidth=0.3)
plt.savefig("comparacion_BAM_ciai_la_granja.png")
