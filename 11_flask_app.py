"""Librería: Flask
Mini servidor web con una página y dos endpoints de API.
Ejecuta el archivo y abre http://127.0.0.1:5000 en el navegador."""
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return "<h1>¡Hola desde Flask!</h1><p>Prueba /api/suma/3/4 y /api/hora</p>"


@app.route("/api/suma/<int:a>/<int:b>")
def suma(a, b):
    return jsonify({"a": a, "b": b, "resultado": a + b})


@app.route("/api/hora")
def hora():
    return jsonify({"hora": datetime.now().strftime("%H:%M:%S")})


if __name__ == "__main__":
    app.run(debug=True)
