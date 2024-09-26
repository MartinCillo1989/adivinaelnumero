from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Variable para almacenar el número secreto
numero_secreto = random.randint(1, 100)
intentos = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global numero_secreto, intentos
    mensaje = ""
    
    if request.method == 'POST':
        intento = request.form.get('intento')
        
        if intento.isdigit():
            intento = int(intento)
            intentos += 1

            if intento < numero_secreto:
                mensaje = "Demasiado bajo. Intenta de nuevo."
            elif intento > numero_secreto:
                mensaje = "Demasiado alto. Intenta de nuevo."
            else:
                mensaje = f"¡Felicidades! Adivinaste el número en {intentos} intentos."
                # Reiniciar el juego
                numero_secreto = random.randint(1, 100)
                intentos = 0
        else:
            mensaje = "Por favor, introduce un número válido."

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
