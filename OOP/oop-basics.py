#OBJECT ORIENTED PROGRAMMING

#Class: Attributes and Methods(functions)
#class definition is a blueprint
#e.g a car would have attributes: id, registration, engine size, purchase price; and methods: accel, brake, turn right etc
#PRIVATE: hidden from user/programmer. All attributes are private
#PUBLIC: Visible for everyone. All methods are public
#GETTER method: return attribute
#SETTER method: assign value to attribute
#OOP FEATURES: Encapsulation, Inheritance, Polymorphism, Containment(aggregation)
#Encapsulation: Hiding attributes from users
#all attributes are private hence encapsulated

#CAR CLASS DECLARATION:
#Constructor is private. No one can call constructor
#__init__: the name of constructor in python
#__ to show smth is priv
class car:
    def __init__(self,i,e):
        self.__carID = i
        self.__registration = ""
        self.__dateOfReg = None
        self.__engineSize = e
        self.__purchasePrice = 0

    #Getter method: a method to access its associated attribute
    #return the attribute
    def getCArID(self):
        return self.__carID
    def getRegistration(self):
        return self.__registration
    def getDateOfReg(self):
        return self.__registration

    def getEngineSize(self):
        return self.__engineSize
    def getPurchasePrice(self):
        return self.__purchasePrice

    #Setter method: a method to set the value of its associated attribute
    #parameter value is assigned to attribute
    #since carId shouldn't change so no set method
    def setRegistraion(self,r):
        self.__registration = r
    def setDateOfReg(self,date):
        self.__dateOfReg = date
    #engine size shouldn't change so no set method
    def setPurchasePrice(self,price):
        self.__purchasePrice = price

myCar = car("BBZ 527",1233)
print(myCar.getEngineSize(),myCar.getPurchasePrice()) #add () after the methods. right now getPurchasePrice will output 0 as assigned above

myCar.setPurchasePrice(100000)
print(myCar.getPurchasePrice()) #now it will output the assigned value

#can also be written as
myCarEngine = myCar.getEngineSize()
print(myCarEngine)
