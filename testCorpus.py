
# corpus  REDDIT 

# chargement de la librairie

import praw
praw.__version__

# s'identifier

reddit = praw.Reddit(client_id='Q-hGVHp0E7hJfaBlGF4xKw', client_secret='DMbe1oti1MLFfTbv-oxn4-NxnAAfHg', user_agent='proj_prog_python')

# Requête
subs = reddit.subreddit("all")

for submission in subs.hot(limit=None):
    print("************")
    print(submission.title)


# Récupération du texte
docu = []
docus_bruts = []
affichageCles = False
for i, post in enumerate(subs):
    if i%10==0: print("Reddit:", i, "/", limit)
    if affichageCles:  
        for k, v in post.__dict__.items():
            pass
            print(k, ":", v)

    if post.selftext == "":  
        continue
    docu.append(post.selftext.replace("\n", " "))
    docus_bruts.append(("Reddit", post))



# corpus ArXiv
# Libraries
import urllib, urllib.request, _collections
import xmltodict

# Parametres
queryTerms = ["clustering", "Dirichlet"]
maxResults = 100

# Requete de l'url
url = f'http://export.arxiv.org/api/query?search_query=all:{"+".join(query_terms)}&start=0&max_results={max_results}'
data = urllib.request.urlopen(url)

# Format dict 
data = xmltodict.parse(data.read().decode('utf-8'))


# Ajout de la liste
for i, entry in enumerate(data["feed"]["entry"]):
    if i%10==0: print("ArXiv:", i, "/", limit)
    docs.append(entry["summary"].replace("\n", ""))
    docs_bruts.append(("ArXiv", entry))


#  Exploitation 

print(f" : {len(docs)}")
docs = list(set(docs))
print(f" : {len(docs)}")

for i, doc in enumerate(docs):
    print(f"Document {i}\t : {len(doc)}\t : {len(doc.split(' '))}\t : {len(doc.split('.'))}")
    if len(doc)<100:
        docs.remove(doc)

longueChaineDeCaracteres = " ".join(docs)



# classe document

from Classes import Document

# manip de la classe

import datetime
collection = []
for nature, doc in docs_bruts:
    if nature == "ArXiv":  

        titre = doc["title"].replace('\n', '') 
        try:
            authors = ", ".join([a["name"] for a in doc["author"]])  
        except:
            authors = doc["author"]["name"]  
        summary = doc["summary"].replace("\n", "") 
        date = datetime.datetime.strptime(doc["published"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")  

        doc_classe = Document(titre, authors, date, doc["id"], summary)  
        collection.append(doc_classe)  


 elif nature == "Reddit":
       
        titre = doc.title.replace("\n", '')
        auteur = str(doc.author)
        date = datetime.datetime.fromtimestamp(doc.created).strftime("%Y/%m/%d")
        url = "https://www.reddit.com/"+doc.permalink
        texte = doc.selftext.replace("\n", "")

        doc_classe = Document(titre, auteur, date, url, texte)

        collection.append(doc_classe)

# Création de l'index de documents
id2doc = {}
for i, doc in enumerate(collection):
    id2doc[i] = doc.titre

# classe auteur

from Classes import Author

# creation d'un dictionnaire auteur
authors = {}
aut2id = {}
num_auteurs_vus = 0

# Création de la liste des Auteurs
for doc in collection:
    if doc.auteur not in aut2id:
        num_auteurs_vus += 1
        authors[num_auteurs_vus] = Author(doc.auteur)
        aut2id[doc.auteur] = num_auteurs_vus

    authors[aut2id[doc.auteur]].add(doc.texte)


# corpus  

from Corpus import Corpus
corpus = Corpus("mes corpus")

# Construction d'un corpus a partir des documents
for doc in collection:
    corpus.add(doc)




#  POLYMORPHISME 
from Classes import ArxivDocument, RedditDocument
nouveauDocReddit = RedditDocument(titre="Titre Reddit",
                                  date=datetime.datetime.now(),
                                  url="http://urlreddit.com",
                                  texte="il s'agit d'un contenu Reddit",
                                  nbCommentaires=12)
nouveauDocArxiv = ArxivDocument(titre="Titre Arxiv",
                                date=datetime.datetime.now(),
                                url="http://urlarxiv.com",
                                texte="il s'agit d'un ArXiv",
                                liste_auteurs=["Auteur 1", "Auteur 2"])


corpus.add(nouveauDocReddit)
corpus.add(nouveauDocArxiv)

print(nouveauDocArxiv.get_type())
print(nouveauDocReddit.get_type())







