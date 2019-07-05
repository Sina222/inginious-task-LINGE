def arrToMat(tab):
    Mat=[[0 for j in range(len(tab))] for i in range(len(tab))]
    for i in range(len(tab)): 
        for j in range(i):
            Mat[i][j] = tab[i]
            Mat[j][i] = tab[i]
        Mat[i][i] = tab[i]
    return Mat

"""
a=arrToMat([1,2,3,4,5])
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end=" ")
    print()


1	2	3	4	5	
2	2	3	4	5	
3	3	3	4	5	
4	4	4	4	5	
5	5	5	5	5
"""