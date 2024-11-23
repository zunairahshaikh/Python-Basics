#Inheritance: all attributes and methods of the base class are copied to the subclass
#BASE CLASS / PRENT CLASS: MAin class from which other class will copy
#SUB / CHILD CLASS: class that inherits / copies the attributes and methods from the base class
#e.g library item could be a book or cd

import datetime
class libraraItem:
    def __init__(self,a,id,title):
        self.__itemID = id
        self.__itemTitle = title
        self.__authorArtist = a
        self.__onLoan = False
        self.dueDate = datetime.date.today()