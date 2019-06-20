from math import*
a = int(input("Ingrese el valor de a:"))
b = int(input("Ingrese el valor de b:"))
c = int(input("Ingrese el valor de c:"))
p = (a+b+c)/2
print ("El perimetro es:", p)
s = (int(sqrt((p*(p-a)*(p-b)*(p-c)))))
print("La superficie es:", s)

