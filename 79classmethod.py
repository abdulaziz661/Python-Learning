class Name:

    def _init_(self,first, middle, last):
       self.first = first
       self.middle = middle
       self.last = last

    def _str_(self):
       return self.first + ' ' + self.middle + ' ' + self.last

aName = Name('mary') 
print(Name)

