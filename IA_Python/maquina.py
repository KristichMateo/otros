import tensorflow as tf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

celsius = np.array([-40,-10,0,8,15,22,38],dtype=float)
farenheit = np.array([-40,14,32,46,59,72,100],dtype=float)
capa = tf.keras.layers.Dense(units=3,input_shape=[1]) #Creo capa densa con 3 unidades neuronales, indico que es de entreada
capa_oculta = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1) 
modelo = tf.keras.Sequential([capa,capa_oculta,salida])
modelo.compile(     #Creo compilador
    optimizer=tf.keras.optimizers.Adam(0.1), #Creo optimizador, utilizo Adam(Ranago de correccions)
    loss="mean_squared_error" #funcion de perdida (pocos errores grandes peor que muchos errores pequeño)
)
print("entrenamiento")
historial = modelo.fit(celsius,farenheit, epochs=1000,verbose=False) #entreno el modelo, digo datos de entreda, esperados, verbose = false para que no impima
print("modelo entrenado")
resultado = modelo.predict([100.0])#Predice un resultado para una entrda
print("es resultado es",resultado)
print(capa.get_weights()) #obtiene peso y cesgo (formula resolvente)
plt.xlabel("epoca")
plt.ylabel("errores")
plt.plot(historial.history["loss"]) # grafico lso errores alo largo del tiempo
plt.show()