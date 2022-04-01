def aire_rectangle(largeur,longueur):
    return largeur*longueur

a=input()
b=input()
c=aire_rectangle(int(a),int(b))
print("aire d'un rectangle de longueur {} et de largeur {} est de {}".format(a,b,c))
