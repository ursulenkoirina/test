l = [1, 4, 5, 7, 8, 9, 10]
# 1. Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
# 4.1
while l:
    print('Issue4.1: ', l.pop(0))
# 4.2
"""
 ** Как сделать это же задание со строкой: напишите цикл,
который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?
"""
l = 'hello'
while l:
    l = l[1:]
    print(l)

#4.3
"""
Напишите цикл, который выводит на экран и удаляет элементы списка от самого
маленького до самого большого, пока он не останется пустым.
"""
l = [1, 4, 15, 17, 8, 19, 10]

while l:
    l.remove(min(l))
    print(l)
