import yaml

data = {
    'entrypoint': 'main.py',
    'host': 'localhost',
    'port': 8000
}

with open('yaml/conf.yml', 'w') as file:
    yaml.dump(data, file)

with open('yaml/conf.yml') as file:
    print(type(yaml.load(file)))
