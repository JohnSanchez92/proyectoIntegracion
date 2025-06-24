from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Diccionario de tasas
tasas = {
    'USD': 4.0,
    'EUR': 0.9,
    'MXN': 17.0
}

@app.route('/')
def home():
    return 'HOLA MUNDO'  # Sirve el HTML

@app.route('/api/convertir', methods=['POST'])
def convertir():
    data = request.json
    cantidad = data['cantidad']
    origen = data['origen']
    destino = data['destino']

    if origen not in tasas or destino not in tasas:
        return jsonify({'error': 'Moneda no válida'}), 400

    resultado = cantidad / tasas[origen] * tasas[destino]
    return jsonify({'resultado': round(resultado, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
