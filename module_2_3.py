my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
b = len(my_list)
a = 0
while a < b:
    if my_list[a] > 0:
        print(my_list[a])
    elif my_list[a] < 0:
        break
    a = a + 1