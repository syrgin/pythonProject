# a =[1, 2, 3, 4, 5]
# b = []
# print(id(a), id(b))
# a = b
# print(id(a), id(b))
# b.append('123')
# print(a, b)
# print(id(a), id(b))
# ёёimport random
# my_dict = {range(0, 9)}
# my_dict1 = {
#
# }
# print(my_dict)
# my_list = [' павле, пюре, петр, андрей, сергей']
# for i in my_list:
#     if i == 'п':
#         print(i)

my_list = ['колодец', 'ведро', 'кольцо', 'ведро']
sign = []
result = []
for i in my_list:
    if i not in sign:
        sign.append(i)
        result.append(i)
    else:
        if i in result:
            k = result.index(i)
            del result[k]
print(result)
list_1 = [1,2,3,2,3,4,4]
counter = 0
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if list_1[i] == list_1[j]:
            counter += 1
print(counter)
C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)
lst_1 = list(C_1)
lst_2 = list(C_2)
sum(lst_1)
sum(lst_2)
if sum(lst_1) > sum(lst_2):
    print('Сумма больше в кортеже -один')
elif sum(lst_1) < sum(lst_2):
    print('Сумма больше в кортеже -два')
pupils = [
{
'firstname': 'Masha',
'Group': 42,
'physics': 7,
'informatics': 6,
'history': 8,
},
]