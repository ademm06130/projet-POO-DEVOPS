# Projet POO / DevOps – Gestionnaire de Tâches (Client/Serveur)

Ce projet est une application de gestion de tâches développée en Python en architecture **client–serveur**.  
Le client envoie des commandes au serveur (ajout, suppression, affichage…), qui gère les tâches en mémoire via une classe orientée objet.

L’ensemble du projet fonctionne dans **Docker**, avec un `docker-compose` pour lancer facilement le serveur et le client.

---

##  Structure du projet

projet_POO/
client/
      client.py
      Dockerfile.client
server/
      serveur.py
      models.py
      Dockerfile.server
docker/
      Dockerfile
docker-compose.yml
README.md
.gitignore



---

##  Fonctionnalités

###  Côté serveur
- Stockage des tâches via une classe `GestionnaireTaches`
- Commandes supportées :
  - `ADD;Titre;Description;Auteur`
  - `LIST`
  - `DEL;id`
  - `STATUS;id;nouveau_statut`
- Affichage dans le terminal des actions du client (logs simples)

###  Côté client
Menu interactif :
1. Ajouter une tâche  
2. Lister les tâches  
3. Supprimer une tâche  
4. Modifier le statut d’une tâche  
5. Quitter  

Le client communique avec le serveur via des sockets TCP.

---

##  Docker

Les deux composants (client et serveur) fonctionnent dans des conteneurs séparés.

###  **Images Docker Hub**
- Serveur : `adem06/projet_poo_serveur`
- Client : `adem06/projet_poo_client`

---

##  Installation et exécution

### 1️ Cloner le dépôt GitHub

dans le terminal taper:
git clone https://github.com/ademm06130/projet-POO-DEVOPS.git
cd projet-POO-DEVOPS


docker-compose build

Cela va construire les images (si local)

### les methode de lancer le projet

# methode 1 (avec docker-compose)

"taper " docker-compose up "cela va demarer client et serveur ensemble"

ou tu peux demarer separerement

serveur : docker-compose up serveur
et dans une autre terminal
client :docker-compose run client

### methode 2 (avec docker run)

serveur : docker run -it -p 5000:5000 serveur-taches
client : docker run -it --network="host" client-taches

### methode 3 (avec python)
pour le serveur dans le terminal va dans le dossier serveur et tape:
python serveur.py
pour le client dans un autre terminal va dans dossier client et tape :
python client.py

### resultat

Quand le client démarre, un menu apparaît :

=== MENU ===
1. Ajouter une tâche
2. Lister les tâches
3. Supprimer une tâche
4. Changer le statut d'une tâche
5. Quitter
Votre choix :

Il suffit de taper un chiffre puis d’appuyer sur Entrée.


 Exemples de commandes côté serveur

Les messages reçus par le serveur s’affichent automatiquement :

Connexion de ('172.20.0.3', 45812)
[('172.20.0.3', 45812)] Reçu du client : ADD;Course;Acheter du pain;Adem


 Tester les conteneurs séparément

Lancer seulement le serveur

docker-compose up serveur
ou
docker ryn -it -p 5000:5000 serveur-taches

Lancer seulement le client

docker-compose up client
ou
docker run -it --network="host" client-taches

 Arrêter et nettoyer
docker-compose down

 Déploiement sur Docker Hub

Les images ont été publiées avec :

docker build -t adem06/projet_poo_client -f Dockerfile.client .
docker push adem06/projet_poo_client

docker build -t adem06/projet_poo_serveur -f Dockerfile.server .
docker push adem06/projet_poo_serveur

 Auteur
adem mathlouthi RSI2
mohamed sahli RSI2
=======
# Projet POO + Client-Serveur + Docker

## Description
Application de gestion de tâches multi-clients via un serveur Python utilisant sockets.

## Structure du projet
projet_POO/
    server/
    client/
    docker/
    README.md

## Lancer le serveur
python server/serveur.py

## Lancer le client
python client/client.py
