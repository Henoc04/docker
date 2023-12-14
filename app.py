from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simuler une liste d'utilisateurs avec leurs identifiants
users = {
    'henoc': 'motdepasse',
    'utilisateur1': 'motdepasse1',
    'utilisateur2': 'motdepasse2'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Vérification des identifiants
    if username in users and users[username] == password:
        # Authentification réussie, vous pouvez rediriger vers une page de succès par exemple
        return redirect(url_for('success'))
    else:
        # Authentification échouée, vous pouvez rediriger vers une page d'échec ou réafficher le formulaire
        return render_template('login.html', message='Identifiants incorrects')

@app.route('/success')
def success():
    return "Vous êtes connecté avec succès !"

if __name__ == '__main__':
    # Spécifiez le port et l'adresse que vous souhaitez utiliser
    app.run(host='0.0.0.0', port=5000)  # Adresse : 127.0.0.1, Port : 5000
