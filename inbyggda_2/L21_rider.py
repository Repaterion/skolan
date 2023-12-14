from L21_class import person

class rider(person):
    def __init__(self):
        person.__init__(self,0)
        self.__equipment = None

    def setEquipment(self, newEquipment):
        self.__equipment = newEquipment

    def getEquipment(self):
        return self.__equipment

print('Name of module:' + __name__)

r1 = rider()
r1.setAge(10)
r1.setEquipment('Skies')

print(f'Rider 1 is {r1.getAge()} years old and runs {r1.getEquipment()}')
