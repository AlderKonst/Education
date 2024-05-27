pushkin = int(input('Какой год рожения Пушкина? '))
if pushkin == 1799:
    pushkin = float(input('Какой день рожения Пушкина (ДД.ММ)? '))
    if pushkin == 26.05:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')