
# Сформировать одномерный список целых чисел A, используя генератор случайных чисел
# (диапазон от 0 до 99). Размер списка n ввести с клавиатуры.
# В соответствии со своим вариантом написать программу по условию, представленному в таблице ниже.

import random

n = int(input("Введите размер списка n: \n"))
A = [random.randint(0, 99) for i in range(n)]
print(A)

# 1	Удалить элемент с введенным номером a.
a = int(input("Введите номер элемента, который надо удалить: \n"))
item =A.pop(a)
print("Был удален " + str(a) + "-й элемент: " + str(A.pop(a)))
print("Список А после удаления элемента: ")
print(A)

# 2	Все четные по значению элементы исходного списка A поместить в новый список B.
print("\nНовый список В с четными элементами: ")
B = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        b = A[i]
        B.append(b)
print(B)

# 3	Удалить элементы, индексы которых кратны 7.
for i in range(len(A)-1):
    if i % 7 == 0:
        item = A.pop(i)
print("\nСписок А после удаления элементов, индексы которых кратны 7: ")
print(A)

# 4	Найти значение минимального элемента списка.
min = A[0]
i = 1
for i in range(len(A)-1):
    if A[i] < min:
        min = A[i]
print("\nМинимальное значение элемента в списке: " + str(min) + "\n")

# 5	Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом и записать эти суммы в новый список B.
A = [random.randint(0, 99) for i in range(n)]
print("Список А: ")
print(A)
B = []
for i in range(len(A)):
    if i % 2 == 0 and i != 0:
        b = A[i] + A[i + 1]
        item = B.append(b)
print("Список B сумм элементов с четными номерами с последующими элементами: ")
print(B)

# 6	Удалить все элементы с заданным значением, если они имеются в списке.
A = [random.randint(0, 99) for i in range(n)]
print("\nСписок А: ")
print(A)
d = int(input("Введите значение элементов, которые надо удалить: \n"))
q = 0
i = 0
while i < len(A):
    if A[i] == d:
        del A[i]
    else:
        i += 1
print("Список А после удаления элементов с заданным значением: " + str(d))
print(A)

# 7	Удалить из списка все элементы, совпадающие с его минимальным значением.
A_7 = [random.randint(0, 99) for i in range(n)]
print("\nСписок А_7: ")
print(A_7)
min = A_7[0]
i = 1
for i in range(len(A_7)-1):
    if A_7[i] < min:
        min = A_7[i]
print("\nМинимальное значение элемента в списке: " + str(min))

i = 0
while i < (len(A_7)):
    if A_7[i] == min:
        del A_7[i]
    else:
        i += 1
print("\nСписок А_7 после удаления элементов, совпадающие с его минимальным значением: " + str(min))
print(A_7)

# 8	Найти значение максимального элемента списка.
A_8 = [random.randint(0, 99) for i in range(n)]
print("\nСписок А_8: ")
print(A_8)
max = A_8[0]
i = 1
for i in range(n):
    if A_8[i] > max:
        max = A_8[i]
print("\nМаксимальное значение элемента в списке: " + str(max))

# 9	Найти среднее арифметическое элементов списка.
A_9 = [random.randint(0, 99) for i in range(n)]
print("\nСписок А_9: ")
print(A_9)
i = 0
s = 0
av_sum = 0
for i in range(n):
    s = sum(A)
    av_sum = s/len(A_9)
print("\nСреднее арифметическое элементов списка: " + str(av_sum))

# 10	Найти среднее арифметическое трех последних элементов списка.
# 11	Удалить пять первых нечетных по значению элементов списка.
# 12	Найти номер минимального элемента списка.
# 13	Найти для каждого элемента списка А сумму предыдущих элементов и записать эти суммы в новый список B.
# 14	Найти индексы первого и последнего нулевых элементов списка.
# 15	Удалить элементы, индексы которых кратны 3.
# 16	Найти номера минимального и максимального элементов первой половины списка.