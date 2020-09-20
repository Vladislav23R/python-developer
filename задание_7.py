import json

list_result = []
with open("задание_7.json", "w", encoding="utf-8") as f_obj:
    with open("задание_7.txt", encoding="utf-8") as file:
        profit = {}
        average = {}
        loss = {}
        for line in file:
            a = line.rstrip("\n").split(" ") # отбрасываем пробелы и перенос строки
            if int(a[2]) >= int(a[3]):
                profit[a[0]] = int(a[2]) - int(a[3]) # считаем прибыль компании
            if int(a[2]) < int(a[3]):
                loss[a[0]] = int(a[2]) - int(a[3]) # считаем убыток компании
        average["average_profit"] = sum(profit.values()) / int(len(profit))
        list_result.append(profit)
        list_result.append(average)
        list_result.append(loss)
        # print(profit)
        # print(list_result)
    json.dump(list_result, f_obj)








