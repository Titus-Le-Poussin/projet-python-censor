import random
List_debut = {"Espece","Sac","Bougre","Tête","Tronche","Crotte"}
List_adjectif = {"Vieux","Gros","Fou","Lumineux","spongieux","mou","radioactif","sombre","malefique","gélatineux","gluant","Malodorant"}
List_Nom_Rigolos = {"Lama","Nouille","Champignon","Cornichon","Limace","Chausette"}
List_mot_entre = {"de","à","et","le","la","les","des","du"}

debut = random.choice(list(List_debut))
Adjectif = random.choice(list(List_adjectif))
Nom_Rigolos = random.choice(list(List_Nom_Rigolos))
List_mot_entre = random.choice(list(List_mot_entre))


for i in range(2):
    Phrase = f"{debut} de {Nom_Rigolos} {Adjectif}"
    print(Phrase)


