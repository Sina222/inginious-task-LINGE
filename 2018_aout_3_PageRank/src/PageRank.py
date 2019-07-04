class PageRank:

    def OutdegreeVector(self,A):
        Dout = [0 for i in range(len(A))]
        for i in range(len(A[0])):
            for j in range(len(A)):
                Dout[i]=Dout[i]+A[i][j]
        return Dout

    def IndegreeVector(self, A):
        Din = [0 for i in range(len(A))]
        for i in range(len(A[0])):
            for j in range(len(A)):
                Din[i]=Din[i]+A[j][i]
        return Din

    def ProbabilityMatrix(self,A):
        P = []
        temp=[]
        D = self.OutdegreeVector(A)
        for i in range(len(A)):
            for j in range(len(A[0])):
                temp.append(A[i][j]/D[i])
            P.append(temp)
            temp=[]
        return P

    def Transpose (selt, P):
        Pt=[[0 for j in range(len(P[0]))] for i in range(len(P))]
        for i in range(len(P)):
            for j in range(len(P[0])):
                Pt[i][j] = P[j][i]
        return Pt

    def produitMatriceVecteur(self, A,d):
        if len(A[0]) != len(d):
            #print("erreur, matrice non conforme")
            return None
        else:
            c = [0 for i in range(len(d))]
            for i in range(len(A)):
                for k in range(len(A[0])):
                    c[i] += A[i][k]*d[k]   
            return c
        
    def normalize (self, d):
        c = [0 for i in range(len(d))]
        sum=0.0
        for j in range(len(d)):
            sum = sum + d[j]
        for j in range(len(d)):
            c[j]=d[j]/sum
        return c

    def PageRankScore(self,A):
       P = self.ProbabilityMatrix(A)
       Pt = self.Transpose(P)
       score = self.normalize(self.IndegreeVector(A)) 
       diffscore = 1
       oldscore=[]
       while (diffscore > 0.000001):
            oldscore=score   
            score =  self.produitMatriceVecteur(Pt,oldscore)
            diffscore = 0
            for i in range(len(score)):
                diffscore = diffscore + abs(score[i]-oldscore[i])
       return score    
"""
A = [[0,1,1],[1,5,0],[0,1,2]]
PageRank_correct=PageRank()

print(str(A))
a=Q3Aout2018()
print("out")
print(str(a.OutdegreeVector(A)))
print("Proba")
P=a.ProbabilityMatrix(A)
print(P)
print("Transpose:")
print(a.Transpose(P))
Din = a.normalize(a.IndegreeVector(A)) 
print("Noramlize")
print(str(Din))
score = a.PageRankScore(A)
print("PageRank")
print(str(score))


score = PageRank_correct.IndegreeVector(A)
prod_Mat_Vec_correct=PageRank_correct.produitMatriceVecteur(A,score) #test 2
print(prod_Mat_Vec_correct)
"""