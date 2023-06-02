from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
y= []
x= 0
fun=input("ingrese su funcion")
fun=2+5*x/(3*4)

def plot(): 
    
    
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    for i in range(15):
        global x
        x =+ 1
        y.append(fun)
    
    
    
    
    plot1 = fig.add_subplot(111) 
  
    
    plot1.plot(y) 
  
    
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    
    canvas.get_tk_widget().pack() 
  
    
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    
    canvas.get_tk_widget().pack() 
    
  
window = Tk() 
  
window.title('Plotting in Tkinter') 
  
window.geometry("500x500") 
  
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Magia") 
  
plot_button.pack() 
  
window.mainloop()