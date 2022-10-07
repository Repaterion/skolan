#### FÖRÄLDRAKLASSEN ####
class component:
    def __init__(self, x, y, label):
        #self.__location = int(location)
        self.__locationX = x ###MÅSTE VARA SAMMA SOM I __init__.
        self.__locationY = y
        self.__label = label

    def setLocation(self, x, y):
        self.__locationX = x
        self.__locationY = y
        #platsLista = ""
    
    def setLoc(self, setLoc):
        return [self.__locationX, self.__locationY]

    def getLoc(self):
        return [self.__locationY, self.__locationX]

    def getLabel(self):
        return self.__label

    def printComponent(self):
        print(f'Coocrdinates {str(self.__locationX)} and {str(self.__locationY)}')

def main(): #### MÅSTE STÅ UTAN ARGUMENT ANNARS FUNGERAR DET INTE.
    c1 = component(0,0, 'comp1')
    c2 = component(5,5, 'comp2')
    print(f'{c1.getLabel()} is located at {str(c1.getLoc())}')
    print(f'{c2.getLabel()} is located at {str(c2.getLoc())}')

if __name__ == '__main__':
    main()
