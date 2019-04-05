import yaml

data = {
    'first_key': ['first_value', 'second_value'],
    'second_key': 8000,
    'third_key': {
        'lira': '1₤',
        'euro': '2€',
        'bitcoin': '3₿'
    }
}

with open('Data/file.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=True, allow_unicode=True)

with open('Data/file.yml') as file:
    print(yaml.load(file))
