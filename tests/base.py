import yaml


def read():
    with open('../cassette-example.yml', 'r') as f:
        return yaml.safe_load(f.read())



def write():
    cassette = read()
    
    with open('../cassette-example.py', 'w') as f:
        f.write(yaml.dump(cassette))


read()
write()