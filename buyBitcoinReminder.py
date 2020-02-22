from gi.repository import Notify
from urllib import request
import requests
import csv
import time

#Affiche la notification pour Gnome
def notificationAlerte(value):
    if value <= 20:
        titre = "URGENT - Bitcoin"
        message = "Il faut acheter du bitcoin aujourd'hui!"
    elif value <= 30:
        titre = "IMPORTANT - Bitcoin"
        message = "Tu peux acheter du bitcoin, c'est le moment"
    elif value <= 40:
        titre= "Bitcoin"
        message="L'achat de bitcoin est à considérer aujourd'hui"
    else:
        titre = "Bitcoin"
        message="N'achètes pas de bitcoin aujourd'hui!"

    Notify.init(titre)
    Hello=Notify.Notification.new (titre + " - " +  message, "L'indice est a " + str(value)   )
    Hello.show ()


time.sleep(5)

#Permet de télécharger le CSV
url = "https://api.alternative.me/fng/"
r = requests.get(url, allow_redirects=True)
open('test.csv', 'wb').write(r.content)


#Lis le CSV et trouve la valeur journalière
fichier = open('test.csv', 'rt')
lecteurCSV = csv.reader(fichier, delimiter=",")
t = 0
for i in lecteurCSV:
    if t ==4:


        value = int(i[0][13] + i[0][14])
        print(value)
    t = t + 1

notificationAlerte(value)


fichier.close()
