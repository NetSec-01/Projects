from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader = FileSystemLoader('.'))
template = ENV.get_template("template.j2")

class Details(object):
    def __init__(self, name, number, email, linked_in):
        self.name = name
        self.number = number
        self.email = email
        self.linked_in = linked_in

class Certifications():
    def __init__(self,certificates):
        self.certificates = input("Enter your certificates,add space after each certificate:")
        print('\n')
        certifi = certificates.split()
        print(certifi)


details_obj = Details("ASLEEM BAIG", "+1-902-802-1987", "asleembaig.ab@gmail.com", "www.linkedin.com/in/asleembaig")
print(template.render(candidate = details_obj))

certification_obj = Certifications("None")
print(template.render(certif = certification_obj))


