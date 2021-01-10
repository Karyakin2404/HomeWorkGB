user_list = input('Введите числа с пробелами - ').split()

for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)
