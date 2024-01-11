###############

#2. Créer un fichier python test.py qui va tester la qualité de prédiction du modèle sur un nouvel échantillon de données (disponible ici https://github.com/AbdallahTayeb/DevOps-Course/blob/main/sample.csv) : 

import pandas as pd
import pickle
import os
from sklearn.metrics import accuracy_score

# Charger le modèle
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Charger ou préparer les données de test
url = "sample.csv"
new_data = pd.read_csv(url,sep=";")
X_new = new_data.drop(columns=['target'])
y_new = new_data['target']
# Faire des prédictions
predictions = model.predict(X_new)

# Calculer la précision
if 'y_new' in locals():
    accuracy = accuracy_score(y_new, predictions)
    print(f"Accuracy on new data: {accuracy:.2f}")

# Définir un seuil de classification
threshold = os.environ(" MY_variable")

# Vérifier si le seuil est atteint
classified_predictions = (predictions > threshold).astype(int)

# Afficher les prédictions classées en fonction du seuil
print("Predictions above threshold:")
print(classified_predictions)

# Vérifier si le seuil est atteint pour chaque prédiction
if 'y_new' in locals():
    accuracy_threshold = accuracy_score(y_new, classified_predictions)
    print(f"Accuracy on new data above threshold: {accuracy_threshold:.2f}")
############

#3. Créer un workflow avec un job build qui va executer bcancer.py et un job test qui va executer test.py
