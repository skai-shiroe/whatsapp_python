import pywhatkit
import time

# Liste de numéros de téléphone
numeros = ['+22897847268', '+22870461628', '+22891490463']  # Ajoutez les numéros que vous souhaitez ici

# Message à envoyer
message = 'happy skai'

# Heure d'envoi (hh, mm)
heure_envoi = 00
minute_envoi = 37

# Temps d'attente initial augmenté
temps_attente_initial = 300

# Boucle à travers chaque numéro
for numero in numeros:
    try:
        # Envoi du message
        pywhatkit.sendwhatmsg(numero, message, heure_envoi, minute_envoi)

        # Ajoutez un délai avant et après chaque envoi
        time.sleep(5)  # Délai avant l'envoi

        print(f"Message WhatsApp envoyé avec succès à {numero}")

        time.sleep(5)  # Délai après l'envoi

    except Exception as e:
        print(f"Erreur lors de l'envoi à {numero}: {e}")
        print(f"Le numéro {numero} pourrait ne pas être sur WhatsApp.")

        # Ajoutez une tentative de reconnexion (facultatif)
        # Si la reconnexion ne fonctionne pas, vous pouvez ajuster cette partie du code
        print("Tentative de reconnexion à WhatsApp Web...")
        pywhatkit.close_tab()
        time.sleep(5)
        pywhatkit.sendwhatmsg(numero, message, heure_envoi, minute_envoi)
        print("Reconnexion réussie. Message WhatsApp envoyé avec succès.")

print("Fin de l'envoi des messages WhatsApp.")




