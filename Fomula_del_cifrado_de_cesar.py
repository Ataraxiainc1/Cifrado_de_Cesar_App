# -*- coding: latin-1 -*-
import tkinter as tk
from tkinter import ttk

# Funci�n de cifrado de C�sar
def cifrar(texto, clave):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = ord('A') if caracter.isupper() else ord('a')
            cifrado = (ord(caracter) - ascii_offset + clave) % 26 + ascii_offset
            resultado += chr(cifrado)
        else:
            resultado += caracter
    return resultado

# Funci�n para cifrar el texto
def cifrar_texto():
    texto_original = entry_texto.get()
    clave = int(entry_clave.get())
    texto_cifrado = cifrar(texto_original, clave)
    label_texto_cifrado.configure(text="Texto Cifrado: " + texto_cifrado)

# Crear la ventana principal
window = tk.Tk()
window.title("Cifrado de C�sar")
window.configure(bg='#171717')

# Configurar estilo tem�tico para el modo oscuro
style = ttk.Style()
style.theme_use('clam')
style.configure('.', foreground='white', background='#171717', font=('Arial', 14, 'bold'), fieldbackground='#1e1e1e')
style.configure('Resultado.TLabel', foreground='orange')

# Agregar un t�tulo con estilo
label_titulo = ttk.Label(window, text="Cifrado de C�sar", font=('Arial', 24, 'bold'), background='#171717', foreground='white')
label_titulo.grid(row=0, column=0, padx=10, pady=10)

# Agregar una imagen creativa relacionada con el cifrado de C�sar
imagen_cesar = tk.PhotoImage(file="cesar.png")
label_imagen_cesar = ttk.Label(window, image=imagen_cesar, background='#171717')
label_imagen_cesar.grid(row=1, column=0, padx=10, pady=10)

# Agregar un campo de texto para ingresar el texto original
label_texto = ttk.Label(window, text="Texto original:", font=('Arial', 16, 'bold'), background='#171717', foreground='white')
label_texto.grid(row=2, column=0, padx=10, pady=5)
entry_texto = ttk.Entry(window, font=('Arial', 16), background='#1e1e1e', foreground='white')
entry_texto.grid(row=3, column=0, padx=10, pady=5)

# Agregar un campo de texto para ingresar la clave de cifrado
label_clave = ttk.Label(window, text="Clave de cifrado:", font=('Arial', 16, 'bold'), background='#171717', foreground='white')
label_clave.grid(row=4, column=0, padx=10, pady=5)
entry_clave = ttk.Entry(window, font=('Arial', 16), background='#1e1e1e', foreground='white')
entry_clave.grid(row=5, column=0, padx=10, pady=5)

# Agregar un bot�n para cifrar el texto
btn_cifrar = tk.Button(window, text="Cifrar", command=cifrar_texto, font=('Arial', 16, 'bold'), background='#1e1e1e', foreground='white')
btn_cifrar.grid(row=6, column=0, padx=10, pady=10)

# Agregar un campo de texto para mostrar el texto cifrado
label_texto_cifrado = ttk.Label(window, text="Texto Cifrado: ", font=('Arial', 16), style='Resultado.TLabel', background='#171717', foreground='orange')
label_texto_cifrado.grid(row=7, column=0, padx=10, pady=5)

# Agregar un enlace a una p�gina web relacionada con el cifrado de C�sar
def abrir_enlace():
    import webbrowser
    webbrowser.open("https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar")

link_label = ttk.Label(window, text="M�s informaci�n sobre el cifrado de C�sar", cursor="hand2", font=('Calibri', 10, 'underline'), background='#171717', foreground='white')
link_label.grid(row=8, column=0, padx=10, pady=5)
link_label.bind("<Button-1>", lambda e: abrir_enlace())

# Ejecutar la ventana
window.mainloop()