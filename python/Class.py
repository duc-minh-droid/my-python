
class Person():
    def __init__(this, name, age):
        this.name = name
        this.age = age
    def getObj(this):
        print({
            'name': this.name,
            'age': this.age
        })

Minh = Person('Minh', 17)
Minh.getObj()

class Coder(Person):
    def __init__(this, name, age, pro):
        super().__init__(name, age)
        this.profession = pro
    def codePy(this): # ALways pass this to a method
        print('Coding...')
    def CodeJs(this):
        print('Coding', this.profession)

Duc = Coder('Duc', 17, 'react')
Duc.CodeJs()













































































