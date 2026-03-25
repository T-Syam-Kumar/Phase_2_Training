class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def helper(self):
        print(self.name)
        print(self.age)
        print(self.marks)


s = student('syam', 20, 100)
e = student('Eswar', 21, 150)
c = student('charan', 19, 500)
print(f'name : {s.name}  age : {s.age} marks: {s.marks}')
print(f'name : {e.name}  age : {e.age} marks: {e.marks}')
print(f'name : {c.name}  age : {c.age} marks: {c.marks}')


# self is used to refer the object in the class