import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(np.random.randint(0,260,size=(400, 1)), columns=["Peso"])


df["Peso"]


























#Calcular la media sin la funcion mean(), a mano chavales
def calculoMedia():
    suma = 0
    for i in df["Peso"]:
        suma = suma + i
    
    return suma/len(df["Peso"])

#Añadir al dataFrame el valor de la media
def añadirMedia():
    df["Media"] = calculoMedia()


#calcular la desviacion sin funcion std()
def calculoDesviacion():
    std = 0
    mean = calculoMedia()
    for i in df["Peso"]:
        std = std + (i - mean)**2
    
    std = std / len(df["Peso"])
    std = np.sqrt(std)
    return std

def desviacionCuadrado():
    df["Desviacion cuadrado"] = desviacion**2
#Añadir a la tabla el valor de la desviación respecto a la media
def añadirDesviacion():
    desviaciones = []
    for i in df["Peso"]:
        desviaciones.append(i - media)

    df["Desviacion"] = desviaciones

def plotDesviacion():
    plt.figure(figsize=(10,10))
    sns.histplot(df["Desviacion"])
    plt.show()
    plt.pie(df["Peso"])
    plt.show()


media = calculoMedia()
añadirMedia()

desviacion = calculoDesviacion()
añadirDesviacion()

desviacionCuadrado()

plotDesviacion()

df.to_csv("Datos.csv")


































data = pd.DataFrame()
lista = [1,2,5,678,6564]
data["Numeros"] = lista
data.to_csv("ey.csv")