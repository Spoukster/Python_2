import os
import csv

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []


def get_data():
    # Перебираем все файлы в папке Data
    for data_file in os.listdir('Data/'):
        # Если имя файла начинается с info, то открываем файл
        if data_file.startswith('info'):
            with open('Data/' + data_file, encoding='windows-1251') as file:
                # Если строка начинается с нужного значения, то записываем в соответсвующий список
                for line in file:
                    if line.startswith('Изготовитель системы'):
                        line = line.split(':')[1].strip()
                        os_prod_list.append(line)
                    elif line.startswith('Название ОС'):
                        line = line.split(':')[1].strip()
                        os_name_list.append(line)
                    elif line.startswith('Код продукта'):
                        line = line.split(':')[1].strip()
                        os_code_list.append(line)
                    elif line.startswith('Тип системы'):
                        line = line.split(':')[1].strip()
                        os_type_list.append(line)

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    # Высчитываем длину максимально длинного списка
    max_len = len(max(os_prod_list, os_name_list, os_code_list, os_type_list, key=lambda x: len(x)))

    # Формируем лист с значениями и добавляем в главный список
    for i in range(max_len):
        temp_list = []
        temp_list.append(os_prod_list[i])
        temp_list.append(os_name_list[i])
        temp_list.append(os_code_list[i])
        temp_list.append(os_type_list[i])
        main_data.append(temp_list)

    return main_data


def write_to_csv(link):
    data = get_data()
    with open(link, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(data)


write_to_csv('report.csv')
