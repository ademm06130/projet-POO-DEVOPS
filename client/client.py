import socket

class ClientTaches:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = por

    def envoyer(self, message):
        try:
            s = socket.socket()
            s.connect((self.host, self.port))
            s.send(message.encode())
            reponse = s.recv(4096).decode()
            s.close()
            return reponse
        except Exception as e:
            return f"Erreur client : {e}"

def menu():
    client = ClientTaches()

    while True:
        print("\n=== MENU ===")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Supprimer une tâche")
        print("4. Changer le statut d'une tâche")
        print("5. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            titre = input("Titre : ")
            description = input("Description : ")
            auteur = input("Auteur : ")
            message = f"ADD;{titre};{description};{auteur}"
            print(client.envoyer(message))

        elif choix == "2":
            print(client.envoyer("LIST"))

        elif choix == "3":
            id_tache = input("ID de la tâche à supprimer : ")
            print(client.envoyer(f"DEL;{id_tache}"))

        elif choix == "4":
            id_tache = input("ID de la tâche : ")
            statut = input("Nouveau statut (TODO/DOING/DONE) : ")
            print(client.envoyer(f"STATUS;{id_tache};{statut}"))

        elif choix == "5":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")




if __name__ == "__main__":
    menu()
