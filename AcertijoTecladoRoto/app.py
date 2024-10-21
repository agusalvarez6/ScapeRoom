from flask import Flask, render_template, request
from logic import inicializar_historial, procesar_acertijo, procesar_entrada_alterada

app = Flask(__name__)

# Inicializar variables globales
estado = 0  # 0 = primer acertijo, 1 = segundo acertijo con teclado alterado
historial_mensajes = inicializar_historial()

@app.route('/', methods=['GET', 'POST'])
def index():
    global estado, historial_mensajes

    if request.method == 'POST':
        if estado == 0:  # Primer acertijo
            respuesta = request.form.get('respuesta')
            estado, historial_mensajes = procesar_acertijo(respuesta, historial_mensajes)
        elif estado == 1:  # Segundo acertijo con teclado alterado
            entrada = request.form.get('entrada')
            estado, historial_mensajes = procesar_entrada_alterada(entrada, historial_mensajes)

    return render_template('console.html', estado=estado, historial_mensajes=historial_mensajes)

if __name__ == '__main__':
    app.run(debug=True)
