# найти простые числа

# number = int(input())
# new_List = []
# counter = 0
# for i in range(1, number + 1):
#     simple = True
#     for j in range(2, i):
#         counter += 1
#         if i % j == 0:
#             simple = False
#             break
#     if simple:
#         new_List.append(i)
# print(new_List)
# print(counter)


def findSimpleNumber(number):
    counter = 0
    for i in range(1, number + 1):
        simple = True
        for j in range(2, i):
            counter += 1
            if i % j == 0:
                simple = False
                break
        if simple:
            new_List.append(i)
    return new_List


new_List = []
n = int(input())
print(findSimpleNumber(n))
