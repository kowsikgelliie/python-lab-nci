class Greeting:
    name = ""
    def __init__(self,name) -> None:
        self.name = name
    def greeting(self) -> None:
        print(f"Hey {self.name} nice to meet you.")

obj = Greeting(input("What is your name?"))
obj.greeting()