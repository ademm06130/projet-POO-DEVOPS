import socket
from models import GestionnaireTaches

gestionnaire = GestionnaireTaches()

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "0.0.0.0"
PORT = 5000
serveur.bind((HOST, PORT))
serveur.listen()

print(f"Serveur démarré sur {HOST}:{PORT}...")

while True:
    client, adresse = serveur.accept()
    print("Connexion de", adresse)

    msg = client.recv(1024).decode().strip()
    print("Message reçu:", msg)

    if msg.startswith("ADD;"):
        try:
            _, titre, description, auteur = msg.split(";", 3)
            t = gestionnaire.ajouter_tache(titre, description, auteur)
            client.send(f"Tâche ajoutée avec id {t.id}".encode())
        except Exception as e:
            client.send(f"Erreur ajout tâche: {e}".encode())

    elif msg == "LIST":
        taches = gestionnaire.lister_taches()
        client.send(str(taches).encode())

    elif msg.startswith("DEL;"):
        try:
            _, id_str = msg.split(";")
            id_tache = int(id_str)
            if gestionnaire.supprimer_tache(id_tache):
                client.send(f"Tâche {id_tache} supprimée".encode())
            else:
                client.send(f"Tâche {id_tache} introuvable".encode())
        except Exception as e:
            client.send(f"Erreur suppression: {e}".encode())

    elif msg.startswith("STATUS;"):
        try:
            _, id_str, nouveau_statut = msg.split(";")
            id_tache = int(id_str)
            if gestionnaire.changer_statut(id_tache, nouveau_statut):
                client.send(f"Tâche {id_tache} mise à jour en {nouveau_statut}".encode())
            else:
                client.send(f"Tâche {id_tache} introuvable".encode())
        except Exception as e:
            client.send(f"Erreur changement statut: {e}".encode())
    else:
        client.send("Commande inconnue".encode())

    client.close()
