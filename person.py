class Person:
  def innit (self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender


def introduce(self):
    print(f"Hi there! My name is {self.name}.I am {self.age} years old and I am {self.gender} ")




person1=Person('Bethuel',18,'Male')
person2=Person('Kemboi',28,'Male')
person3=Person('Annette',24,'Female')

person1.introduce()
