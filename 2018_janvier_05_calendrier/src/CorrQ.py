class Date:
    def __init__(self, jour,mois,annee):
        self.__jour=jour
        self.__mois=mois
        self.__annee=annee

    def getJour(self):
        return self.__jour
    
    def getMois(self):
        return self.__mois
    
    def getAnnee(self):
        return self.__annee

    def hier(self):
        if self.__jour !=1:
            self.__jour-=1
        else:
            # On vérifie si on est le 1 mars d'une année bissextile
            if (((self.getAnnee()%4 == 0 and self.getAnnee()%100 != 0) or self.getAnnee()%400 == 0) and (self.getMois()==3)):
                self.__jour=29
                self.__mois=2
            else:
                # On vérifie si on est le 1 mars pour passer au 28 février
                if(self.getMois()==3 and self.getJour()==1):
                    self.__jour=28
                    self.__mois=2

                # On vérifie si on est dans un mois qui suit un mois de 31 jours et le premier jour de ce mois
                if (self.getMois()==2 or self.getMois()==4 or self.getMois()==6 or self.getMois()==9 or self.getMois()==11 or self.getMois()==8 ):
                    self.__jour=31
                    self.__mois=self.__mois-1
                
                # On vérifie si on est dans un mois qui suit un mois de 30 jours et le premier jour de ce mois
                if ( self.getMois()==5 or self.getMois()==7 or self.getMois()==10 or self.getMois()==12):
                    self.__jour=30
                    self.__mois=self.__mois-1

                # On vérifie si on est le 1 janvier pour revenir le 31/12 une année en arrière
                if(self.getMois()==1 and self.getJour()==1):
                    self.__jour=31
                    self.__mois=12
                    self.__annee=self.__annee-1

    def __str__(self):
        return "Jour: {} Mois: {} Année: {}".format(self.getJour(),self.getMois(),self.getAnnee())
