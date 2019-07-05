def merge(tab1, tab2):
    sol =[0 for i in range(len(tab1)+len(tab2))] 
    if len(tab1)<len(tab2):
        for i in range(len(tab1)):
            sol[2*i] = tab1[i]
            sol[2*i+1] = tab2[i]

        for i in range(len(tab1),len(tab2)):
            sol[len(tab1)+i] = tab2[i]
    else:
        for i in range(len(tab2)):
            sol[2*i] = tab1[i]
            sol[2*i+1] = tab2[i]

        for i in range(len(tab2),len(tab1)):
            sol[len(tab2)+i] = tab1[i]
    return sol
