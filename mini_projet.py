# mini_projet.py
import json
def menu ():
     print("le menu gestion de classe  :")
     print("1:afficher tous les étudiants .")
     print("2:ajouter un étudiant .")
     print("3:supprimer un étudiant par son indice .")
     print("4:mettre à jour un étudiant  .")
     print("5:calculer/afficher statistiques (moyenne, meilleure note, etc) .")
     print("6:rechercher un étudiant par nom .")
     print("q:quitter .")
     choix =input("entrer votre choix : ")
     return choix
def afficher_classe(classe):
     if not classe :
          print("la classe est vide .")
          return
     for index ,(nom,age ,note) in enumerate(classe,start=1):
          print(f"{index}.{nom}-{age} ans -note{note}")
     with open ("classe.json","w") as f:
          json.dump(dictionnaire, f,indent=0)
def ajouter_etudiant (classe):
     nom=input("Nom: ").strip()
     try :
          age =int (input (" age : "))
          note =float(input("Note: "))
     except ValueError:
          print("saisie invalide .")
          return
     classe.append([nom,age,note])
     print(f"{nom} ajoute .")
     with open ("classe.json","w") as f:
          json.dump(dictionnaire, f,indent=0)
def supprimer_etudiant(classe):
     if not classe :
          print("la classe est vide ")
          return
     try :
          index =int (input("donner l'indice de l'etudiant que vous voulez supprimer (premier indice c'est 0 !)" ))
          reponse=input(f"voulez-vous  vraiment supprimer l'étudiant d'indice {index} (oui/non)")
          if reponse =="oui":
               etudiant=classe.pop(index)
               print(f"{etudiant[0]} supprime")
     except (ValueError,IndexError):
          print("index invalide ")
     with open ("classe.json","w") as f:
          json.dump(dictionnaire, f,indent=0)
def mettre_a_jour_etudiant(classe):
     if not classe:
          print("classe vide ")
          return
     try :
          index =int (input ("donner l'indice de l'etudiants que vous voulez modifiee"))-1
          etudiant=classe[index]
     except (ValueError,IndexError):
          print("indice invalide .")
          return
     print(f"Modification de {etudiant[0]} (laisser vide pour ne pas changer")
     noueau_nom=input ("nouveau nom :").strip()
     if noueau_nom:
          etudiant[0] = noueau_nom
     entree_age=input("nouvel age :").strip()
     if entree_age:
          try:
               etudiant[1] = int(entree_age)
          except ValueError:
               print("Âge ignoré (saisie invalide).")
     entree_note = input("Nouvelle note : ").strip()
     if entree_note:
          try:
               etudiant[2] = float(entree_note)
          except ValueError:
               print("Note ignorée (saisie invalide).")
     with open ("classe.json","w") as f:
          json.dump(dictionnaire, f,indent=0)
def afficher_statistiques(classe):
     if not classe:
          print("Pas de données.")
          return
     notes = [etudiant[2] for etudiant in classe]
     moyenne = sum(notes) / len(notes)
     meilleure = max(classe, key=lambda e: e[2])
     pire = min(classe, key=lambda e: e[2])
     print(f"Moyenne des notes : {moyenne:.2f}")
     print(f"Meilleure note : {meilleure[2]} ( {meilleure[0]} )")
     print(f"Moins bonne note : {pire[2]} ( {pire[0]} )")
     with open ("classe.json","w") as f:
          json.dump(dictionnaire, f,indent=0)
def recherche_nom(classe):
     Not_in=0
     if not classe:
          print("Pas de données.")
          return
     nom_cherche=input("donner le nom que vous cherchez").strip()
     for nom,age ,note in classe :
          if nom==nom_cherche:
               print(f"le nom que vous cherchez  existe:nom->{nom},age->{age},note->{note}")
               Not_in+=1
               break
     if Not_in==0:
          print(f"le nom {nom_cherche} n'existe pas dans la classe .")

     with open ("classe.json","w") as f:
          json.dump(dictionnaire, f,indent=0)
     
classe =[
     ["Alice",20,15.5],
     ["Eve",19,14.0],
     ["Charlie",21,16.5]
]
classe.append(["Diana",17,13])
dictionnaire={nom :(age,note) for nom ,age ,note in classe }
while True :
     choix =menu()
     if choix == "1":
          afficher_classe(classe)
     elif choix == "2":
          ajouter_etudiant(classe)
     elif choix == "3":
          supprimer_etudiant(classe)
     elif choix == "4":
          mettre_a_jour_etudiant(classe)
     elif choix == "5":
          afficher_statistiques(classe)
     elif choix == "6":
          recherche_nom(classe)
     elif choix == "q":
          print("Au revoir.")
          break
     else:
          print("choix invalide.")

