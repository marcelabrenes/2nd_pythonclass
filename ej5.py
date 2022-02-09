#Realice un programa que dada la base y la altura de un rectángulo,calcule el área y el perímetro de este.

base=int(input("The base of the rectangle is:"))
height=int(input("The height of this rectangle is:"))
Area=base*height 
Perimeter=2*(base+height)
print("The area of the rectangle is:",Area)
print("The perimeter of the rectangle is:",Perimeter)