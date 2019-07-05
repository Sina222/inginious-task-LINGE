def sousChaine(x, y):
    sizeX = len(x)
    sizeY = len(y)
    if sizeX<sizeY:
        return False
    i = 0
    indexY = 0
    while i < sizeX and indexY < sizeY:
        if y[indexY]==x[i]:
            indexY = indexY+1
        i = i+1
    
    if indexY==sizeY:
        return True
    else:
        return False