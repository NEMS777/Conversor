print("Programa de covnersion de undiades de Longitud")
print("Sellecione la unidad de entrada \n 1: Metros \n 2: Pies \n 3: Centimetros \n 4: Kilometros")


num=int(input("Ingrese el numero correspondeinte a la unidad: \n"))
canti=int(input("Ingrese la cantidad a covnertir: \n"))


print("Sellecione la unidad de salida \n 1: Metros \n 2: Pies \n 3: Centimetros \n 4:Kilometros")

num2=int(input("Ingrese el numero correspondeinte a la unidad: \n "))


uni={"1":" metros",2:" pies",3:" centimetros",4:" kilometros"}

if num==1:
    conver={1:1,2:3.28084,3:100,4:0.001}
    print(str(canti)+" metros son "+str(canti*conver[num2])+uni[num2])
if num==2:
    conver={1:0.3048,2:1,3:30.48,4:0.0003048}
    print(str(canti)+" pies son "+str(canti*conver[num2])+uni[num2])
if num==3:
    conver={1:0.01,2:0.0328084,3:1,4:0.00001}
    print(str(canti)+" centimetros son "+str(canti*conver[num2])+uni[num2])
if num==4:
    conver={1:1000,2:3280.84,3:100000,4:1}
    print(str(canti)+" kilometros son "+str(canti*conver[num2])+uni[num2])
if num>4:
    print("no ha escogido ninguna opcion")
if num2>4:
    print("no ha escogido ninguna opcion")