'''etudiants=["Alice","Bob","Charlie"]
print(etudiants)
etudiants.append("Diania")
print(etudiants)
if "Bob" in etudiants:
     etudiants.remove("Bob")
     print(etudiants)
dernier=etudiants.pop()
print(etudiants)
print(etudiants[0])
print(etudiants[-1])
print(etudiants[-2])
notes =[16,18,11,10,9]
print(notes[1:4])
print(notes[:3])
print(notes[3:])
#un element sur 2
print(notes[::2])
#l'inverse de la liste 
print(notes[::-1])'''
classe =[
     ["Alice",20,15.5],
     ["Eve",19,14.0],
     ["Charlie",21,16.5]
]
classe.append(["Diana",17,13])
print(classe)
for index ,(nom,age,note) in enumerate (classe,start=1):
     print(f"Etudiant{index}->{nom} -> {age} ans -> note {note}")
age_charlie=classe[2][1]
print(age_charlie)
if classe[2][2]:
     classe[2][2]=16
     print(classe[2][2])
for etudiant in classe:
     print(etudiant[0], etudiant[2])

