

from Classes.etudiant import*
#creer liste etudiant
#aficher liste etudiant

etud1 = Etudiant()
etud1.nom = "Morand"
etud1.prenom = "Honiel"
etud1.no_dossier = "01003"

etud2 = Etudiant()
etud2.nom = "Graville"
etud2.prenom = "Stanley"
etud2.no_dossier = "01005"

etud3= Etudiant() 
etud3.nom = "Sainterlin"
etud3.prenom = " Edson"
etud3.no_dossier = "01004"

etud4= Etudiant() 
etud4.nom = "MITIAL"
etud4.prenom = "Obenson"
etud4.no_dossier = "01003"



etudiant = []
etudiant.append(etud1)
etudiant.append(etud2)
etudiant.append(etud3)
etudiant.append(etud4)


for etud in etudiant:
    etud.present_to()
