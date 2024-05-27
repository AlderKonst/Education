lst_1 = input(f'Введите элементы первого списка через запятую: ').replace(' ', '').split(',')
lst_2 = input(f'Введите элементы второго списка через запятую: ').replace(' ', '').split(',')
for i in range(len(lst_1) - 1, -1, -1):
    if lst_1[i] in lst_2:
            lst_1.remove(lst_1[i])
print(lst_1)