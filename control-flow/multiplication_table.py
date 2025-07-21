number = int(input("Enter a number to see its multiplication table: "))

for j in range(1, 11):
    i = number * j
    print(f"{number} * {j} = {i}")
