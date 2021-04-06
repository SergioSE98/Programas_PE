# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:40:14 2021

@author: Sergio
"""

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
#Leo los archivos de datos

gravim_data = pd.read_csv("filtros_hvs_20_4_10-intervalo_20200601-20201231_SCO_.csv", header=0, sep = ", ", engine = "python", )

beta_data = pd.read_csv("202006_202012_Beta_Raw_Data.csv", header=0)

meteo_data = pd.read_csv("202006_202012_Meteo_SCO.csv", header=0)


#Los datos de gravimetrico se tomaron el 30/12 pero no los de radiación beta, me quito ese elemento
#print(gravim_data)
gravim_data = gravim_data.drop([46])
#print(gravim_data)





#Asigno parámetros a las columnas de interés

pm_gravim = gravim_data["PM"]

pm_beta = beta_data["pm"]
id_beta = beta_data["id"]
fechas_beta = beta_data["timestampx"]
fechas = pd.to_datetime(fechas_beta)

pm_medio_dias=([])  #Cada índice será un día, empezando por cero, y siguiendo el orden de días del excel de gravimetria
#Ahora creo mascaras y acoto los datos de radiacion beta para los dias en que se realizan medidas de gravimetria

start_date = "2020-09-29 08:00:00"
end_date = "2020-09-30 08:00:00"
mask_29_09 = (fechas >= start_date)&(fechas <= end_date)
beta_data_29_09 = beta_data[mask_29_09]
pm_beta_29_09 = beta_data_29_09["pm"]
pm_medio_dias.append(np.mean(pm_beta_29_09))


start_date = "2020-07-27 08:00:00"
end_date = "2020-07-28 08:00:00"
mask_27_07 = (fechas >= start_date)&(fechas <= end_date)
beta_data_27_07 = beta_data[mask_27_07]
pm_beta_27_07 = beta_data_27_07["pm"]
pm_medio_dias.append(np.mean(pm_beta_27_07))


start_date = "2020-06-13 08:00:00"
end_date = "2020-06-14 08:00:00"
mask_06_13 = (fechas >= start_date)&(fechas <= end_date)
beta_data_06_13 = beta_data[mask_06_13]
pm_beta_06_13 = beta_data_06_13["pm"]
pm_medio_dias.append(np.mean(pm_beta_06_13))

start_date = "2020-06-17 08:00:00"
end_date = "2020-06-18 08:00:00"
mask_06_17 = (fechas >= start_date)&(fechas <= end_date)
beta_data_06_17 = beta_data[mask_06_17]
pm_beta_06_17 = beta_data_06_17["pm"]
pm_medio_dias.append(np.mean(pm_beta_06_17))


start_date = "2020-06-21 08:00:00"
end_date = "2020-06-22 08:00:00"
mask_06_21 = (fechas >= start_date)&(fechas <= end_date)
beta_data_06_21 = beta_data[mask_06_21]
pm_beta_06_21 = beta_data_06_21["pm"]
pm_medio_dias.append(np.mean(pm_beta_06_21))


start_date = "2020-06-25 08:00:00"
end_date = "2020-06-26 08:00:00"
mask_06_25 = (fechas >= start_date)&(fechas <= end_date)
beta_data_06_25 = beta_data[mask_06_25]
pm_beta_06_25 = beta_data_06_25["pm"]
pm_medio_dias.append(np.mean(pm_beta_06_25))


start_date = "2020-06-29 08:00:00"
end_date = "2020-06-30 08:00:00"
mask_06_29 = (fechas >= start_date)&(fechas <= end_date)
beta_data_06_29 = beta_data[mask_06_29]
pm_beta_06_29 = beta_data_06_29["pm"]
pm_medio_dias.append(np.mean(pm_beta_06_29))


start_date = "2020-07-07 08:00:00"
end_date = "2020-07-08 08:00:00"
mask_07_07 = (fechas >= start_date)&(fechas <= end_date)
beta_data_07_07 = beta_data[mask_07_07]
pm_beta_07_07 = beta_data_07_07["pm"]
pm_medio_dias.append(np.mean(pm_beta_07_07))


start_date = "2020-07-11 08:00:00"
end_date = "2020-07-12 08:00:00"
mask_07_11 = (fechas >= start_date)&(fechas <= end_date)
beta_data_07_11 = beta_data[mask_07_11]
pm_beta_07_11 = beta_data_07_11["pm"]
pm_medio_dias.append(np.mean(pm_beta_07_11))

start_date = "2020-07-15 08:00:00"
end_date = "2020-07-16 08:00:00"
mask_07_15 = (fechas >= start_date)&(fechas <= end_date)
beta_data_07_15 = beta_data[mask_07_15]
pm_beta_07_15 = beta_data_07_15["pm"]
pm_medio_dias.append(np.mean(pm_beta_07_15))


start_date = "2020-07-19 08:00:00"
end_date = "2020-07-20 08:00:00"
mask_07_19 = (fechas >= start_date)&(fechas <= end_date)
beta_data_07_19 = beta_data[mask_07_19]
pm_beta_07_19 = beta_data_07_19["pm"]
pm_medio_dias.append(np.mean(pm_beta_07_19))


start_date = "2020-07-23 08:00:00"
end_date = "2020-07-24 08:00:00"
mask_07_23 = (fechas >= start_date)&(fechas <= end_date)
beta_data_07_23 = beta_data[mask_07_23]
pm_beta_07_23 = beta_data_07_23["pm"]
pm_medio_dias.append(np.mean(pm_beta_07_23))


start_date = "2020-07-31 08:00:00"
end_date = "2020-08-01 08:00:00"
mask_07_31 = (fechas >= start_date)&(fechas <= end_date)
beta_data_07_31 = beta_data[mask_07_31]
pm_beta_07_31 = beta_data_07_31["pm"]
pm_medio_dias.append(np.mean(pm_beta_07_31))


start_date = "2020-08-04 08:00:00"
end_date = "2020-08-05 08:00:00"
mask_08_04 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_04 = beta_data[mask_08_04]
pm_beta_08_04 = beta_data_08_04["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_04))


start_date = "2020-08-08 08:00:00"
end_date = "2020-08-09 08:00:00"
mask_08_08 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_08 = beta_data[mask_08_08]
pm_beta_08_08 = beta_data_08_08["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_08))


start_date = "2020-08-12 08:00:00"
end_date = "2020-08-13 08:00:00"
mask_08_12 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_12 = beta_data[mask_08_12]
pm_beta_08_12 = beta_data_08_12["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_12))


start_date = "2020-08-16 08:00:00"
end_date = "2020-08-17 08:00:00"
mask_08_16 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_16 = beta_data[mask_08_16]
pm_beta_08_16 = beta_data_08_16["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_16))


start_date = "2020-08-20 08:00:00"
end_date = "2020-08-21 08:00:00"
mask_08_20 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_20 = beta_data[mask_08_20]
pm_beta_08_20 = beta_data_08_20["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_20))

start_date = "2020-08-24 08:00:00"
end_date = "2020-08-25 08:00:00"
mask_08_24 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_24 = beta_data[mask_08_24]
pm_beta_08_24 = beta_data_08_24["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_24))


start_date = "2020-08-28 08:00:00"
end_date = "2020-08-29 08:00:00"
mask_08_28 = (fechas >= start_date)&(fechas <= end_date)
beta_data_08_28 = beta_data[mask_08_28]
pm_beta_08_28 = beta_data_08_28["pm"]
pm_medio_dias.append(np.mean(pm_beta_08_28))


start_date = "2020-09-01 08:00:00"
end_date = "2020-09-02 08:00:00"
mask_09_01 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_01 = beta_data[mask_09_01]
pm_beta_09_01 = beta_data_09_01["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_01))


start_date = "2020-09-05 08:00:00"
end_date = "2020-09-06 08:00:00"
mask_09_05 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_05 = beta_data[mask_09_05]
pm_beta_09_05 = beta_data_09_05["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_05))


start_date = "2020-09-09 08:00:00"
end_date = "2020-09-10 08:00:00"
mask_09_09 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_09 = beta_data[mask_09_09]
pm_beta_09_09 = beta_data_09_09["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_09))


start_date = "2020-09-13 08:00:00"
end_date = "2020-09-14 08:00:00"
mask_09_13 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_13 = beta_data[mask_09_13]
pm_beta_09_13 = beta_data_09_13["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_13))


start_date = "2020-09-17 08:00:00"
end_date = "2020-09-18 08:00:00"
mask_09_17 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_17 = beta_data[mask_09_17]
pm_beta_09_17 = beta_data_09_17["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_17))


start_date = "2020-09-21 08:00:00"
end_date = "2020-09-22 08:00:00"
mask_09_21 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_21 = beta_data[mask_09_21]
pm_beta_09_21 = beta_data_09_21["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_21))


start_date = "2020-09-25 08:00:00"
end_date = "2020-09-26 08:00:00"
mask_09_25 = (fechas >= start_date)&(fechas <= end_date)
beta_data_09_25 = beta_data[mask_09_25]
pm_beta_09_25 = beta_data_09_25["pm"]
pm_medio_dias.append(np.mean(pm_beta_09_25))


start_date = "2020-10-03 08:00:00"
end_date = "2020-10-04 08:00:00"
mask_10_03 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_03 = beta_data[mask_10_03]
pm_beta_10_03 = beta_data_10_03["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_03))


start_date = "2020-10-07 08:00:00"
end_date = "2020-10-08 08:00:00"
mask_10_07 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_07 = beta_data[mask_10_07]
pm_beta_10_07 = beta_data_10_07["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_07))


start_date = "2020-10-11 08:00:00"
end_date = "2020-10-12 08:00:00"
mask_10_11 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_11 = beta_data[mask_10_11]
pm_beta_10_11 = beta_data_10_11["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_11))


start_date = "2020-10-15 08:00:00"
end_date = "2020-10-16 08:00:00"
mask_10_15 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_15 = beta_data[mask_10_15]
pm_beta_10_15 = beta_data_10_15["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_15))


start_date = "2020-10-19 08:00:00"
end_date = "2020-10-20 08:00:00"
mask_10_19 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_19 = beta_data[mask_10_19]
pm_beta_10_19 = beta_data_10_19["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_19))


start_date = "2020-10-23 08:00:00"
end_date = "2020-10-24 08:00:00"
mask_10_23 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_23 = beta_data[mask_10_23]
pm_beta_10_23 = beta_data_10_23["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_23))


start_date = "2020-10-27 08:00:00"
end_date = "2020-10-28 08:00:00"
mask_10_27 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_27 = beta_data[mask_10_27]
pm_beta_10_27 = beta_data_10_27["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_27))


start_date = "2020-10-31 08:00:00"
end_date = "2020-11-01 08:00:00"
mask_10_31 = (fechas >= start_date)&(fechas <= end_date)
beta_data_10_31 = beta_data[mask_10_31]
pm_beta_10_31 = beta_data_10_31["pm"]
pm_medio_dias.append(np.mean(pm_beta_10_31))


start_date = "2020-11-12 08:00:00"
end_date = "2020-11-13 08:00:00"
mask_11_12 = (fechas >= start_date)&(fechas <= end_date)
beta_data_11_12 = beta_data[mask_11_12]
pm_beta_11_12 = beta_data_11_12["pm"]
pm_medio_dias.append(np.mean(pm_beta_11_12))


start_date = "2020-11-16 08:00:00"
end_date = "2020-11-17 08:00:00"
mask_11_16 = (fechas >= start_date)&(fechas <= end_date)
beta_data_11_16 = beta_data[mask_11_16]
pm_beta_11_16 = beta_data_11_16["pm"]
pm_medio_dias.append(np.mean(pm_beta_11_16))


start_date = "2020-11-20 08:00:00"
end_date = "2020-11-21 08:00:00"
mask_11_20 = (fechas >= start_date)&(fechas <= end_date)
beta_data_11_20 = beta_data[mask_11_20]
pm_beta_11_20 = beta_data_11_20["pm"]
pm_medio_dias.append(np.mean(pm_beta_11_20))


start_date = "2020-11-24 08:00:00"
end_date = "2020-11-25 08:00:00"
mask_11_24 = (fechas >= start_date)&(fechas <= end_date)
beta_data_11_24 = beta_data[mask_11_24]
pm_beta_11_24 = beta_data_11_24["pm"]
pm_medio_dias.append(np.mean(pm_beta_11_24))


start_date = "2020-12-14 08:00:00"
end_date = "2020-12-15 08:00:00"
mask_12_14 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_14 = beta_data[mask_12_14]
pm_beta_12_14 = beta_data_12_14["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_14))


start_date = "2020-12-02 08:00:00"
end_date = "2020-12-03 08:00:00"
mask_12_02 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_02 = beta_data[mask_12_02]
pm_beta_12_02 = beta_data_12_02["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_02))


start_date = "2020-12-06 08:00:00"
end_date = "2020-12-07 08:00:00"
mask_12_06 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_06 = beta_data[mask_12_06]
pm_beta_12_06 = beta_data_12_06["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_06))


start_date = "2020-12-10 08:00:00"
end_date = "2020-12-11 08:00:00"
mask_12_10 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_10 = beta_data[mask_12_10]
pm_beta_12_10 = beta_data_12_10["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_10))


start_date = "2020-12-18 08:00:00"
end_date = "2020-12-19 08:00:00"
mask_12_18 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_18 = beta_data[mask_12_18]
pm_beta_12_18 = beta_data_12_18["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_18))


start_date = "2020-12-22 08:00:00"
end_date = "2020-12-23 08:00:00"
mask_12_22 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_22 = beta_data[mask_12_22]
pm_beta_12_22 = beta_data_12_22["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_22))


start_date = "2020-12-26 08:00:00"
end_date = "2020-12-27 08:00:00"
mask_12_26 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_26 = beta_data[mask_12_26]
pm_beta_12_26 = beta_data_12_26["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_26))

"""
start_date = "2020-12-30 08:00:00"
end_date = "2020-12-31 08:00:00"
mask_12_30 = (fechas >= start_date)&(fechas <= end_date)
beta_data_12_30 = beta_data[mask_12_30]
pm_beta_12_30 = beta_data_12_30["pm"]
pm_medio_dias.append(np.mean(pm_beta_12_30))
"""

start_date = "2020-11-08 08:00:00"
end_date = "2020-11-09 08:00:00"
mask_11_08 = (fechas >= start_date)&(fechas <= end_date)
beta_data_11_08 = beta_data[mask_11_08]
pm_beta_11_08 = beta_data_11_08["pm"]
pm_medio_dias.append(np.mean(pm_beta_11_08))




#Ajuste lineal


print(pm_medio_dias)
print(pm_gravim)
ajuste = np.polyfit(pm_gravim,pm_medio_dias,1)
print(ajuste)
y_ajuste=([])
for i in  range(len(pm_gravim)):
      if i == 46: 
          calculo = ajuste[0]*pm_gravim[47] + ajuste[1]
          y_ajuste.append(calculo)
          break

      calculo = ajuste[0]*pm_gravim[i] + ajuste[1]
      y_ajuste.append(calculo)

#print(len(y_ajuste))

plt.figure()
plt.plot(pm_gravim, pm_medio_dias, ".", label = "Datos")
plt.plot(pm_gravim, y_ajuste, label= "Ajuste (a=%.3f, b=%.3f)" %(ajuste[0],ajuste[1]))
plt.xlabel("PM10 medido por el método de referencia (gravimétrico)")
plt.ylabel("PM10 medido por el método automático")
plt.legend()
plt.grid(linewidth=0.3)
plt.title("Verificación/corrección del método de atenuación beta")
plt.savefig("Verificación_corrección del método de atenuación beta.png")
























