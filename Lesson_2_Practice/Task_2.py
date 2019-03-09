import json


def write_order_to_json(item='', quantity='', price='', buyer='', date=''):
    # Формируем словарь заказа
    order_data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('Data/orders.json') as file:
        orders = json.load(file)
        orders['orders'].append(order_data)  # Добавляем заказ в список заказов
    with open('Data/orders.json', 'w') as file:
        json.dump(orders, file, indent=4)


write_order_to_json(item='Book', quantity=2, price=100, buyer='Buyer_1', date='10.03.2019')
