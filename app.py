from flask import Flask
import pandas, numpy

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bonjour Henoc'

if __name__ == '__main__':
    # Spécifiez le port et l'adresse que vous souhaitez utiliser
    app.run(host='0.0.0.0', port=80)  # Adresse : 127.0.0.1, Port : 5000