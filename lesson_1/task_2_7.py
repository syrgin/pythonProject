# a = int(input('Vvedite semishnachnoe chislo'))
# if a % 2 == 0:
#         print(a)
# a = 'тартарары'
# s = 'зарплата'
# print(s*10)
# print(a)
# b = a.split('р')
# print(b)
# print(''.join(b))
# a = 'рено'
# b = 'внимательность'
# # s = len(b)
# # print(s)
# # print(a[2::-1] + a[3:2:-1] + b[0] + b[9:])
# print(b[13])
# print(b.rfind('н'))
# a = 'каркаркаркаркаркаркаркаркаркаркаркаркаркаркаркар'
# print(len(a))
# print(a.count('к'))
# a = 'dfgdgffg'
# print(a.startswith('d'))
# print(a.endswith('g'))
# a = input('VVedide musik').lower()
# if a == 'musik':
#     print(('tyG\nTug\ntYg') * 3)
# for i in range(10):
#     print(i , 'Hello')
a = int(input('Ввдети семизначное число'))
summ = 0
mult = 1
if a > 0:
        for i in str(a):
                if int(i) % 2 == 0:
                        summ += int(i)
                elif int(i) % 2 != 0:
                        mult *= int(i)
print(f"Результат = {summ} {mult}")
# a = int(input())
# summ = 0
# if len(a) % 2:
#         for i in str(a):
#                 if int(i) % 2 == 0:
#                         summ += int(i)
#                         print(f" htp = {summ}")
