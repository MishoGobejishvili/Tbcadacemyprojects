
# 1.გადაჭერით მეხუთე დავალების მეორე ამოცანა while ციკლის გამოყენები:
# დაწერეთ პროგრამა რომელიც დაბეჭდავს გამრავლების ტაბულას 1 და 9 ის ჩათვლით.
# ტაბულა უნდა იყოს სვეტებად შედგენილი. ყოველ მომდევნო სვეტში არ უნდა იყოს გამეორებული ნამრავლი წინა სვეტიდან.

i = 1

while i < 10:
    j = 1
    while j < i + 1:
        print(f"{j} * {i} = {i * j}", end=" ")
        j += 1
    i += 1
    print()