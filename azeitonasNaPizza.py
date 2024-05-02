numero=input()
X= int(numero[0])
Y= int(numero[2])
if (X!=Y) and (X>0 and X<100) and (Y>0 and Y<100):
    print("%d %d" % (X, Y))
    print("%d %d" % (Y, X))
    print("%d %d" % (Y, -X))
    print("%d %d" % (X, -Y))
    print("%d %d" % (-X, -Y))
    print("%d %d" % (-Y, -X))
    print("%d %d" % (-Y, X))
    print("%d %d" % (-X, Y))
else :
	print("ERRO")