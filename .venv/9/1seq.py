n = int(input('Количество элементов списка: '))
lst = []
for i in range(n):
    lst.append(float(input(f'Введите {i+1} элемент: ')))
print(sorted(lst))