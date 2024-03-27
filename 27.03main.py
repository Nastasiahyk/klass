#Задание27
import random
array1 = [random.randint(1, 10) for _ in range(17)]
array2 = [random.randint(1, 10) for _ in range(25)]
array3 = list(set(array1 + array2))
print("Первый массив: ", array1)
print("Второй массив:", array2)
print("Третий массив с уникальными элементами:", array3)

#Задание28
import random
m = 5
n = 4
b = [[random.randint(0, 5) for _ in range(n)] for _ in range(m)]
print("Матрица b: ")
for row in b:
    print(row)
non_zero_count = sum([1 for row in b for element in row if element != 0])
print("Количество ненулевых элементов в матрице b: ", non_zero_count)
    # TODO: write code...])