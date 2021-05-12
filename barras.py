from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import *
from pandas import DataFrame

import matplotlib.pyplot as plt

root = Tk()
root.geometry('500x400')
root.title('Grafico de Barras')

framecontenedor = Frame(width='600', height='130', bg='#28E469')
framecontenedor.pack(side='top', anchor='n', padx=1, pady=1)

A=0
B=0

def procesar():
    global A
    global B
    x1 = input_a.get()
    x2 = input_b.get()
    A = int(int(x1)+A)
    B = int(int(x2)+B)
    actualizarGraficoBarras()

def actualizarGraficoBarras():
    global A
    global B
    global barras

    barras.clear()

    #Crear DataFrame
    Data1 = {'Clases':['A','B'], 'Encuesta':[A,B]}
    df1 = DataFrame(Data1, columns=['Clases', 'Encuesta'])
    df1 = df1[['Clases', 'Encuesta']].groupby('Clases').sum()    
    #Agregar datos al grafico
    df1.plot(kind='bar', legend=True, ax=barras)
    barras.set_title('Encuesta')
    bar1.draw()

#Input A
label_a = Label(framecontenedor, text='Clase A:', width='20', font=('bold',10), bg='#28E469')
label_a.place(x=20, y=8)
input_a = Entry(framecontenedor)
input_a.place(x=140, y=10)

#Input B
label_b = Label(framecontenedor, text='Clase B:', width='20', font=('bold',10), bg='#28E469')
label_b.place(x=20, y=40)
input_b = Entry(framecontenedor)
input_b.place(x=140, y=40)

#Button
Button(framecontenedor, text='Graficar', width=20, bg='brown', fg='white', command=procesar).place(x=120, y=80)

#Contenedor de la Grafica
framegraficos = Frame(bg='#949292', width='215', height='620')
framegraficos.pack(side='bottom', anchor='n', padx=1, pady=1)

#Grafico - Valores
Data1 = {'Clases':['A','B'], 'Encuesta':[0,0]}
df1 = DataFrame(Data1, columns=['Clases', 'Encuesta'])
df1 = df1[['Clases', 'Encuesta']].groupby('Clases').sum()

#CrearGrafica
grafico1 = plt.Figure(figsize=(6,5), dpi=50)
barras = grafico1.add_subplot(111)
bar1 = FigureCanvasTkAgg(grafico1, framegraficos)
bar1.get_tk_widget().pack(side='left', fill='both')
df1.plot(kind='bar', legend=True, ax=barras)
barras.set_title('Encuesta')

root.resizable(0,0)
root.mainloop()

