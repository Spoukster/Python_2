import json

data = [
    {
        'name': 'apple',
        'description': 'some apple',
        'cost': 123
    },
    {
        'name': 'apple',
        'description': 'some apple',
        'cost': 123
    },
    {
        'name': 'apple',
        'description': 'some apple',
        'cost': 123
    }
]

# Простой вывод
# with open('json/data.json', 'w') as file:
#     json.dump(data, file)

# Вывод с отступами
# with open('json/data.json', 'w') as file:
#     json.dump(data, file, indent=2)

# Сортировка по ключам
# with open('json/data.json', 'w') as file:
#     json.dump(data, file, sort_keys=True, indent=2)

# Чтение
# with open('json/data.json') as file:
#     print(json.load(file))

# Преобразование в строку
dt = json.dumps(data)

# Кодировка в байтовый тип
dt.encode()
