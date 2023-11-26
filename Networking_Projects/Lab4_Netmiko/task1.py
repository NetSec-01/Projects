import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

hosts = yaml.load(open('hosts1.yml'), Loader = yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader = yaml.SafeLoader)

print(hosts)
print(interfaces)

env = Environment(loader = FileSystemLoader()
