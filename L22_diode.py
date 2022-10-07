from L22_comp import component #IMPORTERING UTAV FÖRÄLDRAKLASSEN.

class diode(component):
    def __init__(self, vf, label ):
        component.__init__(self, x=0, y=0, label = label )
        self.__label = label
        self.__forward = vf


    def vf(self,vf):
        return self.__vf

    def getVf(self):
        return [self.__forward]

    def getLabel(self):
        component.getLabel()

    def setVf(self, vf):
        return self.__setVf

def main():
    d1 = diode(1.6, 'LED')    #### SAMMA SOM CLASSNAMNET #####
    d2 = diode(0.7, 'Kisel diod')
    print(f'Diod {str(d1.getLabel())} placerad vid position: {str(d1.getLoc)}')
    print(f'Diod placerad vid position: {str(d2.getLoc)}')

if __name__ == '__main__':
    main()