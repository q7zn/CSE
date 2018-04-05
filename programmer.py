class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, workplace):
        super(Employee, self).__init__(name, age)
        self.workplace = workplace

    def career(self):
        print("%s goes to work for %s" % self.name, self.workplace)


class Programmer(Employee):
    def __init__(self, name, age, workplace, company):
        super(Programmer, self).__init__(name, age, workplace)
        self.company = company

    def program(self):
        print('%s codes "print("Hello World!") for %s' % self.name, self.company)
