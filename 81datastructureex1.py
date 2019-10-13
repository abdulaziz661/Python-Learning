class Person:
   def _init_(self, name, sex, age):
       self.name = name
       self.sex = sex
       self.age = age

   def _str_(self):
       return self.name + ' ' + self.sex + ' ' + str(self.age)

   def changeName(self, name):
        self.name = name

   def changeAge(self, age):
        self.age = self.age + 1 

Person('Jane Doe','F',23)               

print('person : ' + str(Person))  