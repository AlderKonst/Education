while True:
  n = input('Введите разделитель (запятая, точка с запятой, слэш): ')
  if n in [',', ';', '/']:
    break
  else:
    print('Неверный разделитель, нужна одна из этих: ,;/')
my_lst = input(f'Введите любые цифры через {n}: ').replace(' ', '').split(n)
my_set = {my_lst[i] for i in range(len(my_lst))}
my_str = ', '.join(list(my_set))
print(my_str)