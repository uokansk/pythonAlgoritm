# Необходимо написать алгоритм, считающий сумму всех чисел
# от 1 до N. Согласно свойствам линейной сложности,
# количество итераций цикла будет линейно изменяться
# относительно изменения размера N.

def summaNumbers(n):
    result = 0
    count = 0
    for i in range(n + 1):
        result += i
        count += 1
    return result, count


def summa(n):
    count = 0
    sumNum = n * (n + 1) / 2
    count += 1
    return sumNum, count



number = int(input("Введи число "))
print("Сумма чисел от 1 до", number, "равно", summaNumbers(number))

print("Сумма чисел от 1 до", number, "равно", summa(number))
