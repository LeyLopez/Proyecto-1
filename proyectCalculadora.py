from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.configure(bg="pink")

#Entrada de texto
e_texto = Entry(ventana, font =("Calibri 15"), bg="lavender")
e_texto.grid(row=0, column=0, columnspan=4, padx=15,pady=5)

i=0

#funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i+=1

def borrar():
    e_texto.delete(0, END)
    i=0

def operaciones():
    ecuacion=e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i=0

#botones
boton1=Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1), bg="violet")
boton2=Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2), bg="violet")
boton3=Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3), bg="violet")
boton4=Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4), bg="violet")
boton5=Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5), bg="violet")
boton6=Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6), bg="violet")
boton7=Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7), bg="violet")
boton8=Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8), bg="violet")
boton9=Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9), bg="violet")
boton0=Button(ventana, text="0", width=13, height=2, command=lambda: click_boton(0), bg="violet")

boton_borrar=Button(ventana, text="AC", width=5, height=2, command=lambda: borrar(), bg="purple")
boton_parentesisopen=Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("("), bg="purple")
boton_parentesisoff=Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"), bg="purple")
boton_punto=Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."), bg="purple")

boton_div=Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"), bg="purple")
boton_mult=Button(ventana, text="x", width=5, height=2, command=lambda: click_boton("*"), bg="purple")
boton_sum=Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"), bg="purple")
boton_resta=Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"), bg="purple")
boton_igual=Button(ventana, text="=", width=5, height=2, command=lambda: operaciones(), bg="purple")


boton_borrar.grid(row=1, column=0,padx=5, pady=5)
boton_parentesisopen.grid(row=1, column=1,padx=5, pady=5)
boton_parentesisoff.grid(row=1, column=2,padx=5, pady=5)
boton_div.grid(row=1, column=3,padx=5, pady=5)


boton7.grid(row=2, column=0,padx=5, pady=5)
boton8.grid(row=2, column=1,padx=5, pady=5)
boton9.grid(row=2, column=2,padx=5, pady=5)
boton_mult.grid(row=2, column=3,padx=5, pady=5)

boton4.grid(row=3, column=0,padx=5, pady=5)
boton5.grid(row=3, column=1,padx=5, pady=5)
boton6.grid(row=3, column=2,padx=5, pady=5)
boton_sum.grid(row=3, column=3,padx=5, pady=5)

boton1.grid(row=4, column=0,padx=5, pady=5)
boton2.grid(row=4, column=1,padx=5, pady=5)
boton3.grid(row=4, column=2,padx=5, pady=5)
boton_resta.grid(row=4, column=3,padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2 ,padx=5, pady=5)
boton_punto.grid(row=5, column=2,padx=5, pady=5)
boton_igual.grid(row=5, column=3,padx=5, pady=5)

ventana.mainloop()