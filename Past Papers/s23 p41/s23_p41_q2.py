#Q2ai
class Vehicle:
    # self.__ID :string
    # self.__MaxSpeed :integer
    # self.__CurrentSpeed :integer
    # self.__IncreaseAmount :integer
    # self.__HorizontalPosition : integer
    def __init__(self,id,ms,ia):
        self.__CurrentSpeed = 0
        self.__ID =id
        self.__MaxSpeed = ms
        self.__currentSpeed = 0
        self.__IncreaseAmount = ia
        self.__horizontalPosition = 0

#Q2aii
    def getCurrentSpeed(self): #in exam write exactly like in the question paper
        return self.__currentSpeed
    def getIncreaseAmount(self):
        return self.__IncreaseAmount
    def getHorizontalPosition(self):
        return self.__horizontalPosition
    def getMaxSpeed(self):
        return self.__MaxSpeed

    #Q2aiii
    def setCurrentSpeed(self,currSpeed):
        self.__currentSpeed = currSpeed
    def setHorizontalPosition(self, hp):
        self.__horizontalPosition = hp

    #Q2aiv
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__horizontalPosition += self.__CurrentSpeed

#Q2c
    def outputDetails (self):
        print("Horizontal position: ",self.__horizontalPosition )
        print("Current Speed: ", self.__CurrentSpeed)

#Q2bi
class Helicopter(Vehicle): #inheits Vehicle class so its in brackets
        # self.__VerticalPosition : INTEGER
        # self.__VerticalChange : INTEGER
        # self.__MaxHeight : INTEGER
    def __init__(self,id,ms,ia,vc,mh):
        Vehicle.__init__(self, id, ms, ia)
        self.__VerticalPosition = 0
        self.__VerticalChange = vc
        self.__MaxHeight = mh

#Q2bii
    def IncreaseSpeed(self):
        Vehicle.IncreaseSpeed(self) #base class wala function called here bc it does what the sub class func also has to do
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

#Q2c
    def outputDetails(self):
        Vehicle.outputDetails(self)
        print("Vertical Position:", self.__VerticalPosition)

#Q2d
car = Vehicle("Tiger", 100,20)
heli = Helicopter("Lion",350, 40, 3,100)
car.IncreaseSpeed()
car.IncreaseSpeed() #question asks for speed to be increased twice
car.outputDetails()
heli.IncreaseSpeed()
heli.IncreaseSpeed()
heli.outputDetails()