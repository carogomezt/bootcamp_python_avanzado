from decorators import authenticate_class, validate_password


@authenticate_class
class MyClass:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def say_hello(self):
        print(f"Hi {self.username}, welcome to our system!")

    @validate_password
    def show_password(self):
        print(f"Hi {self.username}, your password starts by: {self.password[:4]}{len(self.password[4:])*'*'}")


my_class = MyClass("carogomezt", "testpwd123")
my_class.say_hello()
my_class.show_password()

# invalid_class = MyClass("codigofacilito", "testpwd")
# invalid_class.say_hello()
# invalid_class.show_password()

