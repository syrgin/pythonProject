# num_1 = int(input('Введите семизначное число'))
# chet = 0
# nechet = 0
# while len(str(num_1)) != 7: or len(num_1) > 7
#         print('Вы ввели не семизначное число')
#         num_1 = int(input('Введите семизначное число'))
# for i in str(num_1):
#         if int(i) % 2 == 0:
#                 chet += 1
#         else:
#                 nechet += 1
# if chet > nechet:
#         sum = 0
#         for i in str(num_1):
#                 sum += int(i)
#         print(sum)
# else:
#         proizv = 0
#         str_num_1 = str(num_1)
#         a = int(str_num_1[0])
#         b = int(str_num_1[2])
#         c = int(str_num_1[5])
#         print(a * b * c)
import re
data = input('Vvedite text')
data = data.lower()
glasn_1 = ['ы','у','а','е','о','э','и','ю','я']
soglas_2 = ['ф','й','ц','в','ч','м']
glcount = 0
sogcount = 0
for string in data:
    for i in glasn_1:
        if string == i:
            glcount += 1
    for i in soglas_2:
        if string == i:
            sogcount += 1
            if glcount == sogcount:
                a = str(glasn_1 f'{'ы','у','а','е','о','э','и','ю','я'})
                print(a)


