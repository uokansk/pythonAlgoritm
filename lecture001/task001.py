# Допустимые делители для числа

number = int(input())
new_List = []

for i in range(1, number + 1):
    print(i)
    if number % i == 0:
        new_List.append(i)
print(new_List)
