a = int(input())  # рубли
b = int(input())  # копейки
n = int(input())  # количество товара
cena = (100 * a) + b
total = cena * n
rub_1 = total // 100
cop_2 = total % 100
print(rub_1, cop_2)
