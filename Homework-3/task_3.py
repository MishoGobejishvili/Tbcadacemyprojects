import random

# 3. დაწერეთ პროგრამა რომელიც გაშვებისას დაბეჭდავს ბანქოს შემთხვევით მნიშვნელობას (სულ 52 შესაძლო მნიშვნელობა:
# 4 ფერი (clubs (♣), diamonds (♦), hearts (♥) and spades (♠)) და 13 მნიშვნელობა
# (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2))

colour = "♣♦♥♠"
value = "AKQJ98765432"

if random.randint(0, 13) == 13:
    print(random.choice(colour), 10)
else:
    print(random.choice(colour), random.choice(value))
