from decimal import Decimal
from math import sqrt

# 3. Დაწერეთ პროგრამა რომელიც მომხმარებელს მისცემს საშუალებას შეიყვანოს პროგრამაში სამკუთხედი გვერდები. Პროგრამამ უნდა დაბეჭდოს ეკრაზე სამკუთხედის ფართობი და პერიმეტრი.

a = Decimal(input("Enter first side of triangle "))
b = Decimal(input("Enter second side of triangle "))
c = Decimal(input("Enter third side of triangle "))
s = (a + b + c) / 2
TriangleArea = sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Area of triangle is {round(TriangleArea, 2)}, Parameter of triangle is {s * 2} \n")
