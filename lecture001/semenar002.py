# Необходимо написать алгоритм поиска всех доступных комбинаций
# (посчитать количество) для количества кубиков K с количеством граней N.

def findAllVariant(num):
    count = 0
    itogo = []
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            for k in range(1, num + 1):
                itogo.append(i)
                itogo.append(j)
                itogo.append(k)
                count += 1
    return count, itogo


def massiv(res):
    return res[1]


res = findAllVariant(int(input()))
res2 = massiv(res)

print(res)
print(res2)


