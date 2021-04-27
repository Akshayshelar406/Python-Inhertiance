class User:
    def __init__(self, name, email, contact):
        self.name = name;
        self.contact = contact
        self.email = email

user = User("Felix", 'felix@gmail.com', 20)

print(user.name, end=" ")
print(user.email, end=" ")
print(user.contact)