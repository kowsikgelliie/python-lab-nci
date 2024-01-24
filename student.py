class Student:
    count = 0
    
    def __init__(self,count) -> None:
        self.count = count
obj = Student(4)
print(obj.count)