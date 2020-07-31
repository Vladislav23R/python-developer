products = []

i = 1
start = None
while start != "Q":
    start = input('Если хотите внести данные введите: Y\n'
                  'Для завершения работы введите: Q\n'
                  'Для аналитики введите: I').upper()
    if start == "Y":
        tuple = (
            i, {'название': input("введите название товара: "),
               'цена': input("введите цену товара: "),
               'количество': input("введите количество товара: "),
               'единицы': input("введите единицы измерения: ")}
        )
        products.append(tuple)
        i += 1
    elif start == "Q":
        break
    elif start =='I':
        name = []
        price = []
        count = []
        ed_iz = []
        i = 0
        analityc = dict(название=name, цена=price, количество=count, единицы=ed_iz)
        while i != len(products):
            name.append(products[i][1]['название'])
            price.append(products[i][1]['цена'])
            count.append(products[i][1]['количество'])
            ed_iz.append(products[i][1]['единицы'])
            i += 1
        print(analityc)
    else:
        print("Вы ввели некорректное значение.")
        continue

print(products)


