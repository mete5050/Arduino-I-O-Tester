x = 2
while x<=53:
    print("const int led"+str(x)+" = "+ str(x)+";")
    x+=1
x = 2
while x<=53:
    print("pinMode(led"+str(x)+" , "+ "OUTPUT);")
    x+=1
x = 2
while x<=53:
    print("digitalWrite(led"+str(x)+" , "+ "LOW);")
    x+=1
