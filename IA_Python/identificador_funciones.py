import tensorflow as tf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
entreda_X = []
salida_Y = []
print("A continuacion ingresara 5 valores en X y 5 valores en Y \n La IA se encargara de encontrar la funcion")
for i in range(5):
    val_x = float(input("ingrese valor de X"))
    print(val_x)
    entreda_X.append(val_x)
    val_y = float(input("ingrese valor de Y"))
    print(val_y)
    salida_Y.append(val_y)

# entreda_X = np.array([-8.2,-7.7,-8.8,40.0,80],dtype=float)
# salida_Y = np.array([3.44,4.566,2.388,100.0,180],dtype=float)
print(entreda_X)
capa = tf.keras.layers.Dense(units=1,input_shape=[1]) #Creo capa densa con 3 unidades neuronales, y una entreada
salida = tf.keras.layers.Dense(units=1) 
modelo = tf.keras.Sequential([capa,salida]) #Creo un modelo secuencial el mas basico con las capas
modelo.compile(     #Creo compilador
    optimizer=tf.keras.optimizers.Adam(0.005), #Creo optimizador, utilizo Adam(Rnago de correccions)
    loss="mean_squared_error" #funcion de perdida (pocos errores grandes peor que muchos errores pequeño)
)
print("entrenamiento")
historial = modelo.fit(entreda_X,salida_Y, epochs=1000,verbose=False) #entreno el modelo, digo datos de entreda, esperados, verbose = false para que no impima
print("modelo entrenado")

print(capa.get_weights()) #obtiene peso y cesgo (formula resolvente)
print(salida.get_weights())
plt.xlabel("epoca")
plt.ylabel("errores")
plt.plot(historial.history["loss"]) # grafico lso errores alo largo del tiempo
plt.show()
a_calcular = float(input("ingrese el numero a calcualar"))
resultado = modelo.predict([a_calcular])#Predice un resultado para una entrda
print("es resultado es",resultado)