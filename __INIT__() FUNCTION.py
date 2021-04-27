class User:
    def __init__(self, name, contact):
        self.name = name;
        self.contact = contact

user = User("Felix", 20)

print(user.name)
print(user.contact)