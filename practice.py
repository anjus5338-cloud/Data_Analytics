class Person:
   def __init__(self,firstname,lastname,age,gender):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.gender = gender


   def printe(self):
     print(self.firstname, self.age) 

person1 = Person("Mahima","Khare",20,"Female")
person2 = Person("Ramesh","Kumar",23,"Male")
person3 = Person("Suresh","Kumar",12,"Male")
person4 = Person("Riya", "Sharma", 19, "Female")

person1.printe()