class User:

    def __init__(self, name, email, contact):
        self.name = name
        self.contact = contact
        self.email = email

    def method1(demo):
        print("Your name is " + demo.name)

user=User()
user.method1()