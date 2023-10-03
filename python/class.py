class hello:

    def __init__(self,name,age):
        self.name=name
        self.age=age  

    def display(self):
        print(self.name)
        print(str(self.age))

class hello2(hello):
    def display2(self):
        print("hello ")

x=hello("prasanth",23)
y=hello2()

x.display()
y.display2()