#integrantes 
#Julio Alexander Maravilla Umañana__USIS018420
#Roberto Fransisco Reyes Palomo____USIS032421
#Joan Steven Gomez Contreras___USIS014921
#Rene Gustavo Garcia Gomez_USIS595218
# IMPORAR LAS LIBRERIAS
import tensorflow as tf 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from urllib import parse
from http.server import HTTPServer, BaseHTTPRequestHandler

Conversor = pd.read_csv("grados_celcius.csv", sep=";")

# Crear los inputs y ouputs
C = Conversor["celsius"]
F = Conversor["fahrenheit"]

class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion GET recibida")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Servidor iniciado en el puerto 3001'.encode())

    def do_POST(self):
        print("POST")
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode()
        data = parse.unquote(data)
        data = float(data)

        predict = modelo.predict([data])
        print('La predicción fue:', predict)
        predict = str(predict[0][0])

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(predict.encode())




# sb.scatterplot(Conversor["celsius"], Conversor["fahrenheit"])

# creando el modelo de entrenamiento
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

# compilar el modelo de entrenamiento
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

# entrenar el modelo de IA
historial = modelo.fit(C, F, epochs=350)

fahrenheit = modelo.predict([1200])


print('Servidor iniciado en el puerto 3001')
server = HTTPServer(('localhost', 3001), servidorBasico)
server.serve_forever()