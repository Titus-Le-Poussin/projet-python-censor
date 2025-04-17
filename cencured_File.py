import random
import pandas as pd

# Chemin vers le fichier Excel
fichier_excel = "C:\\Users\\Utilisateur\\Documents\\informatique\\RandomListPythonCencorFile.xlsx"

# Lire les différentes feuilles du fichier Excel
feuille1 = pd.read_excel(fichier_excel, sheet_name="Feuille1")
feuille2 = pd.read_excel(fichier_excel, sheet_name="Feuille2")
feuille3 = pd.read_excel(fichier_excel, sheet_name="Feuille3")
feuille4 = pd.read_excel(fichier_excel, sheet_name="Feuille4")

# Extraire les colonnes ou données nécessaires
List_debut = feuille1["mot"].dropna().tolist()  
List_adjectif = feuille2["ADJ"].dropna().tolist()  
List_Nom_Rigolos = feuille3["Nom"].dropna().tolist()  
List_mot_entre = feuille4["Determinant"].dropna().tolist()
Genre_ADJ = feuille2["Genre"].dropna().tolist()
Genre_Nom = feuille3["Genre"].dropna().tolist()
Voyelle_ADJ = feuille2["Voyelle"].dropna().tolist()
Voyelle_Nom = feuille3["Voyelle"].dropna().tolist()

# Générer des phrases aléatoires
for i in range(20):
    Nom_Rigolos = random.choice(List_Nom_Rigolos)
    genre_nom_index = List_Nom_Rigolos.index(Nom_Rigolos)
    genre_nom = Genre_Nom[genre_nom_index]

    if Voyelle_Nom[genre_nom_index] == 1:
        Nom_Rigolos = "d'" + Nom_Rigolos
    else:
        Nom_Rigolos = "de " + Nom_Rigolos
    


    if genre_nom == "H":
        adj_filtrés = [adj for adj, genre in zip(List_adjectif, Genre_ADJ) if genre == "H"]
    else:
        adj_filtrés = [adj for adj, genre in zip(List_adjectif, Genre_ADJ) if genre == "F"]
        
    Adjectif = random.choice(adj_filtrés)
    debut = random.choice(List_debut)


    Phrase = f"{debut} {Nom_Rigolos} {Adjectif}"
    print(Phrase)