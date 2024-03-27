# 2. პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ სიტყვიდან მხოლოდ თანხმოვანი ასოები.

input_str = input("Enter text: ")

for c in input_str:
    if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u':
        print(c, end="")
