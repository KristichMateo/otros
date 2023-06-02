import tkinter as tk
from tkinter import *

d=0
class Grafico:
    def __init__(self):
        def valor23 ():
            print(self.valor.get())
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, padx=110, pady=5)
        self.valor = tk.StringVar
        self.etiqueta = tk.Label(self.frame, text="¿Es un reclamo o una consulta? ")
        self.etiqueta.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="n")
        
        self.campo = tk.Entry(self.frame, width=30, textvariable=self.valor)
        self.campo.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.boton = tk.Button(self.frame, text="Siguiente", command=print("sdfs"))
        self.boton.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.root.mainloop()

        
    
    
class Consulta:
    def __init__(self):
        pass
if __name__ == "__main__":
    t = Grafico()
    
    
