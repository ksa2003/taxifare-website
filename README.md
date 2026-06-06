# TaxiFare Predictor

## Description

TaxiFare Predictor est une application web développée avec Streamlit permettant d'estimer le prix d'une course de taxi à New York.

L'application récupère les informations saisies par l'utilisateur (date, heure, coordonnées GPS du trajet et nombre de passagers) puis interroge une API de prédiction afin d'obtenir une estimation du tarif.

---

## Fonctionnalités

* Sélection de la date et de l'heure de prise en charge
* Saisie des coordonnées GPS de départ et d'arrivée
* Choix du nombre de passagers
* Visualisation du trajet sur une carte interactive
* Appel d'une API REST de prédiction
* Affichage instantané du tarif estimé

---

## Technologies utilisées

* Python
* Streamlit
* Pandas
* NumPy
* Requests
* API TaxiFare Le Wagon

---

## Structure du projet

```text
.
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Cloner le dépôt :

```bash
git clone <repository_url>
cd taxifare
```

Créer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Lancement de l'application

Exécuter :

```bash
streamlit run app.py
```

L'application sera disponible à l'adresse :

```text
http://localhost:8501
```

---

## Utilisation

1. Choisir la date et l'heure de prise en charge.
2. Saisir les coordonnées GPS du point de départ.
3. Saisir les coordonnées GPS du point d'arrivée.
4. Indiquer le nombre de passagers.
5. Cliquer sur **Predict fare**.
6. Consulter le tarif estimé affiché par l'application.

---

## API utilisée

L'application utilise l'API publique TaxiFare mise à disposition par Le Wagon :

```text
https://taxifare.lewagon.ai/predict
```

L'API reçoit les paramètres suivants :

* pickup_datetime
* pickup_longitude
* pickup_latitude
* dropoff_longitude
* dropoff_latitude
* passenger_count

Elle retourne un objet JSON contenant l'estimation du prix de la course.

---

## Exemple de réponse

```json
{
  "fare": 12.58
}
```

---

## Auteur

Kassim Said Ahmed

Projet réalisé dans le cadre de la formation Data Science / Machine Learning du Wagon.

---
