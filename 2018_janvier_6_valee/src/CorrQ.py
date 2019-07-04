class EXAM_JAN2018_Q3:

    def maximaLocaux(self,tab):
        # Déclaration des variables utilisées dans la méthode
        maximaLocaux = []

        # Première boucle for: identification des maxima locaux
        # Attention : les premier et dernier éléments du tableau ne sont jamais considérés comme des maxima locaux, par simplicité
        for i in range(len(tab)-1): 
            if (tab[i] > tab[i-1] and tab[i] > tab[i+1]):
                maximaLocaux.append(i)
        return maximaLocaux        

    def estVallee(self, tab, a, b):
        isVallee = True
        for i in range(a,b+1):
            # Si on a un point supérieur à la droite, ce n'est pas une vallée ==> estVallee = false
            if(tab[i] > self.valeurDroite(a, tab[a], b, tab[b], i)):
                isVallee = False
        return isVallee

    def valeurDroite(self,xA, yA, xB, yB, x):
        #Calculer la pente
        D=(yB-yA)/(xB-xA)
        return D*(x-xA)+yA

    def plusGrandeVallee(self,tab):
        maxLocaux = self.maximaLocaux(tab)
        resultat = []
        indexDebut,indexFin,longueurPlusGrandeVallee = 0,0,0
        for i in range(0,len(maxLocaux)):
            for j in range(i+1,len(maxLocaux)):
                if(self.estVallee(tab, maxLocaux[i], maxLocaux[j]) and abs(maxLocaux[j] - maxLocaux[i]) > longueurPlusGrandeVallee):
                    indexDebut = maxLocaux[i]
                    indexFin =  maxLocaux[j]
                    longueurPlusGrandeVallee = abs(maxLocaux[j] - maxLocaux[i])
        resultat.append(indexDebut)
        resultat.append(indexFin)
        return resultat


tab = [3, 6, 7, 10, 13, 11, 11, 12, 10, 9, 7, 5, 4, 3, 3, 4, 3,4, 2, 1, 2]
'''
A=EXAM_JAN2018_Q3()
print(str(A.plusGrandeVallee(tab)))
print(str(A.estVallee(tab,4,7)))
print(str(A.estVallee(tab,4,15)))
print(str(A.maximaLocaux(tab)))
'''
