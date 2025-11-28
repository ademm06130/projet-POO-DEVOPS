
class Tache:
    def __init__(self, id, titre, description, auteur):
        self.id = id
        self.titre = titre
        self.description = description
        self.statut = "TODO"   
        self.auteur = auteur

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "description": self.description
            "statut": self.statut,
            "auteur": self.auteur
        }


class GestionnaireTaches:
    def __init__(self):
        self.taches = {}
        self.prochain_id = 1

    def ajouter_tache(self, titre, description, auteur):
        tache = Tache(self.prochain_id, titre, description, auteur)
        self.taches[self.prochain_id] = tache
        self.prochain_id += 1
        return tache

    def lister_taches(self):
        resultat = []
        for t in self.taches.values():
            resultat.append(t.to_dict())
        return resultat

    def supprimer_tache(self, id_tache):
        if id_tache in self.taches:
            del self.taches[id_tache]
            return True
        return False

    def changer_statut(self, id_tache, nouveau_statut):
        if id_tache in self.taches:
            self.taches[id_tache].statut = nouveau_statut
            return True
        return False
