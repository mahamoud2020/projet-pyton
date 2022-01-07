
# les classes et les heritages des corpus (reddit et arxiv)


class Doc:

    # initilaiser les variables de la classe


    def __init__(self, titre="", auteur="", date="", url="", texte="", type=""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

    # modification de la classe mere
        self.type = type

    def get_type(self):
        return self.type
    
    # representation 

    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\t"

    # Fonction qui renvoie le texte à afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur}"


    
    # classe auteur
class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = []
    
    def ajout(self, production):
        self.ndoc += 1
        self.production.append(production)
    def __str__(self):
        return f"Auteur : {self.name}\t : {self


# heritage du corpus reddit

class RedditDocument(Doc):
    def __init__(self, titre="", auteur="", date="", url="", texte="", nbCommentaires=0):
        super().__init__(titre=titre, auteur=auteur, date=date, url=url, texte=texte, type="Reddit") 
        self.nbrCommentaires = nbrCommentaires 


    # les getters

    def get_nbrCommentaires(self):
        return self.nbrCommentaires

    # les setters
    def set_nbrCommentaires(self, val):
        self.nbrCommentaires = val

    # afficher les objets RedditDocument
    
    def __str__(self):
        return f"Document REDDIT : {self.titre}, par {self.auteur}"

    

# heritage du corpus Arxiv

class ArxivDocument(Doc):
    def __init__(self, titre="", date="", url="", texte="", liste_auteurs=None):
        super().__init__(titre=titre, auteur="", date=date, url=url, texte=texte, type="ArXiv") 
        self.liste_auteurs = liste_auteurs

    # les getters
    def get_liste_auteurs(self):
        return self.liste_auteurs

    # les setters
    def set_liste_auteurs(self, val):
        self.liste_auteurs = val

    # Affichage des objets RedditDocument
    
    def __str__(self):
        return f"Document ARXIV : {self.titre}, par {self.liste_auteurs}"










