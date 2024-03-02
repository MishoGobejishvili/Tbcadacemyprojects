import random

# 3. დაწერეთ პროგრამა რომელიც გაშვებისას დაბეჭდავს ბანქოს შემთხვევით მნიშვნელობას (სულ 52 შესაძლო მნიშვნელობა:
# 4 ფერი (clubs (♣), diamonds (♦), hearts (♥) and spades (♠)) და 13 მნიშვნელობა
# (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2))

colour = random.randrange(0, 4)
card = random.randrange(2, 15)

if colour == 0:
    print("clubs ", end="")
elif colour == 1:
    print("diamonds ", end="")
elif colour == 2:
    print("hearts ", end="")
elif colour == 3:
    print("spades ", end="")

if card == 11:
    print("A", end="")
elif card == 12:
    print("K", end="")
elif card == 13:
    print("Q", end="")
elif card == 14:
    print("J", end="")
else:
    print(card)

