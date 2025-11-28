classe =[
     ["Alice",20,15.5],
     ["Eve",19,14.0],
     ["Charlie",21,16.5]
]
classe.append(["Diana",17,13])
classe.sort(key=lambda ligne:ligne[2],reverse=True) #trie des notes par ordre décroissante 
print(f" les notes des étudiants par ordre  décroissante \n : {classe}  ")
moyenne=0
for etudiant in range(len(classe)):   #calcule de la moyenne des notes
     moyenne+=classe[etudiant][2]
moyenne=moyenne/len(classe)
print(f"moyenne des notes de la classe est :{moyenne}")
nom_cherche=input("donner le nom que vous cherchez :")
for nom,age ,note in classe :
     Not_in =0
     if nom ==nom_cherche:
          print(f"le nom que vous cherchez est existe:nom->{nom},age->{age},note->{note}\n")
          Not_in+=1
          break
if Not_in==0:
     print(f"le nom {nom_cherche} n'existe pas dans la classe .")

import copy   
print("création d'une copie de  liste classe : classe_copie .")   
classe_copie=classe[:] #Crée  une copie de classe 
classe_copie[0][1]="Noor"

if classe==classe_copie:
     print(f"les deux listes crées sont identique :\n  classe :{classe}\n=\n classe_copie : {classe_copie}\n")
else :
     print (f"les deux listes sont differentes{classe} != {classe_copie}")
classe_copie2=copy.deepcopy(classe)
classe_copie2[0][1]="Ali"
print(f" la liste Crée  par copy.deepcopy :{classe_copie2}")
print("la transformation de la liste en dictionaire :")
dictionnaire={nom :(age,note) for nom ,age ,note in classe }
print(dictionnaire)
