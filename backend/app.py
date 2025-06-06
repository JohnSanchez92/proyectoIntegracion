from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hola')
def hola():
    return jsonify({'mensaje': 'Hola desde el back'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
