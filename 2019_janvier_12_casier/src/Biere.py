class Biere:
    def __init__(self,nom,alcool):
        self.__nom=nom
        self.__alcool=alcool
        self.__pleine=True

    def boire(self):
        if not self.__pleine:
            print("Vous essayez de boire une biere vide")
        self.__pleine=False
    
    def getNom(self):
        return self.__nom

    def getAlcool(self):
        return self.__alcool

    def estPleine(self):
        return self.__pleine
    
    def __str__(self):
        return "Nom: {}  Alcool: {}".format(self.__nom, self.__alcool)
