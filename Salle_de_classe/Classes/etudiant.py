
class Etudiant:
    nom = ""
    prenom = ""
    no_dossier = ""
    
    
    def getNomComplet(self):
        return self.nom+ "" + self.prenom
    
    def _init_(self, nom, prenom, no_dossier):
        self.nom = nom
        self.prenom = prenom
        self.no_dossier = no_dossier 

    
    def _str_(self):
        return"[{self.nom}, {self.prenom},{self.no_dossier}]".format(self= self)



    def present_to( self):
        print("Nom:", self.nom )
        print("prenom", self.prenom )
        print("no_dossier:", self.no_dossier )
        print("__________________________\n")
    
    
        
    