name_1 = input('Сколько Вам лет? ')
if name_1 <= '0':
    print('Wrong input')
elif name_1 < '18':
    print('CocaCola')
else:
    print('Beer')