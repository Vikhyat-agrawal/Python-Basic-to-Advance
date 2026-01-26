class greeting:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def say_hello():
        return f"good morning"
obj = greeting("Alice")
print(obj.say_hello())  # Output: good morning