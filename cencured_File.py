import random
debut = {"Espèce","Sac","Bougre","Tête","Morceau","Tronche","Bete","Crotte","Vieux","Petit"}
adjectif = {"Vieux","Gros","Fou","Lumineux","spongieux","mou","radioactif","sombre","maléfique","gélatineux","gluant","Malodorant"}
Nom_Rigolos = {"Lama","Nouille","Champignon","Cornichon","Limace","Chausette"}
mot_entre = {"de","à","et","le","la","les","des","du"}

Phrase = f"{random.choice(list(debut))} {random.choice(list(mot_entre))} {random.choice(list(adjectif))} {random.choice(list(Nom_Rigolos))}"
print(Phrase)
print("probleme")
