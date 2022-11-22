from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"



# age = age des personnes 
# job = type d'emploi
# maritial = situation marital
# education = niveau d'éducation scolaire
# default = a-t-il un crédit
# balance = argent sur son compte
# housing = a-t-il un prêt maison
# loan = a-t-il un prêt
# contact = moyen de communication
# day = dernier contact le jour
# month dernier contact le mois
# duration dernier contact en seconde
# campaign = nombre de contacts effectués pendant cette campagne et pour ce client
# pdays = nombre de jours depuis le dernier contact
# previous = nombre de contacts effectués avant cette campagne et pour ce client
# poutcome = resultat de la campagne marketing
# target = le client a-t-il souscrit à un prêt