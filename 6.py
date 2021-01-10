goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0

while True:
    if input('Для выхода из приложения нажмите Q, для продолжения Enter: ').upper() == 0:
        break
    num += 1
    for f in features.keys():
        prop = input(f'Введите значение свойства {f} - ')
        features[f] = input(prop) if (f == 'цена' or f == 'количество') else prop
        analytics[f].append((num, features))
    goods.append((num, features))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам:\n{'*' * 30}")
    for key, value in analytics.items():
        print(f"{key[:25]:>30}: {value}")
    print('*' * 30)
