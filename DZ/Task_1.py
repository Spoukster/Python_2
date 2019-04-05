import os

for file_name in os.listdir('../Data'):
    if file_name.startswith('info'):
        with open(file_name, encoding='utf-8') as file:
            print(file)
