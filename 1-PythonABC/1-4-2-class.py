class Man:
    def __init__(self, name):
        self.name = name
        print("initialized")

    def hello(self):
        print("Hello" + self.name + "!")
    def hello_template(self):
        print(f"Hello {self.name}!")
    
    def goodbye(self):
        print("Goodbye" + self.name + "!")
    def goodbye_template(self):
        print(f"Goodbye {self.name}!")

m = Man("me")
m.hello()
m.goodbye_template