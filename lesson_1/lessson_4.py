# for i in range(10):
#     print(i+1, '----Привет')
# import time
# time.sleep()
# for i in range(10):
#     import time
#     time.sleep(1)
#     print(i+1, 'Хороший день сегодня')
# # for i in range(10):
#     import time
#     time.sleep(1)
#     print(i+1)
# for i in range(0, 101, 4):
#     if i % 3 ==0:
#         print(i, end='  ')
# for i in range(604800):
#     if i % 2 == 0:
#         hours += 0.5
#     else:
#         hours += 0.7
#         print()


# for i in range(0,10, -1):
#     print(i)
# n = int(input())
# for i in range(n+1):
#     print(f'kwadrat chisla {i} raven {i ** 2}')
n = int(input())
for i in range(n, 0, -1):
    print('*' * i)
