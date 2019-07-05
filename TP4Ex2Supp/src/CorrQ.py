def inverse (a, b):
    if len(a) != len(b):
        print("taille differente !!")
    else:
        x=0
        for i in range(len(a)): 
            x = a[i]
            a[i] = b[i]
            b[i] = x

        print("A = ")
        for i in range(len(a)):
            print(a[i], end=" ")
        print()

        print("B = ")
        for i in range(len(b)):
            print(b[i], end=" ")
        print()
    


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
print("A = ")
for i in range(len(a)):
    print(a[i], end=" ")
print()

print("B = ")
for i in range(len(b)):
    print(b[i], end=" ")
print() 
inverse(a, b)      
    