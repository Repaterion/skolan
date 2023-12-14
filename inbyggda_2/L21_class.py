class person:
    def __init__ (self, age):
        self.__age = int(age)  #### HADE GLÖMT ___ FÖRE AGE.

    def haveBirthday(self):
        self.__age = self.age + 1 #### dubbelt understreck gör den privat

    def beBorne(self):
        self.__age = 0

    def getAge(self):
        return self.__age
    
    def setAge(self, newAge):
        if type(newAge) == int:
            self.__age = newAge
        else:
            print('newAge of wrong type')

def main():
    print('Name of module: ' + __name__)
    p1 = person(input('Hur gammal är person 1? '))
    p2 = person(input('hur gammal är person 2? '))

    print(f'Person 1 är {str(p1.getAge())} gammal')
    print(f'Nu har vi två personer. Sammanslagen ålder {p1.getAge() + p2.getAge()}')

if __name__ == '__main__':
    main()
