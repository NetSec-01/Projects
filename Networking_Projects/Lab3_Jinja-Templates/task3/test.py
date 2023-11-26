import yaml

test = yaml.load(open('/home/kali/Desktop/Templates_lab/Template-lab/task3/data.yml'), Loader = yaml.SafeLoader)
print(type(test))
print(test)
