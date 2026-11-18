import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

ventana.mainloop()