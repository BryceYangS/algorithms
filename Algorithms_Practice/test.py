# class Quardangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#
#     def __del__(self):
#         print('Quardangle object is deleted')
#
# s = Quardangle(1,1,'aa')
# print(s.width)
# del s
# print(s)

# import decimal
#
# print(decimal.Decimal('0.2') + decimal.Decimal('0.1'))

from functools import reduce
print(reduce(lambda x,y: x + y, [0,1,2,3,4]))
print(reduce(lambda x,y : y + x, 'abcde'))

# filter(함수, 리스트)
print(list(filter(lambda x: x < 5, [0,1,2,3,4,5,6])))

a = [-3,-2,-1,0,1,2,3,4]

print( 5 % 2 )
print(list(filter(lambda x: x < 0, a)))
print(list(filter(lambda x: x % 2, range(10))))


# map
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))
