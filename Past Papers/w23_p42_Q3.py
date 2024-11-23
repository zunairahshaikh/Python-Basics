#Q3ai
class Character():
    def __init__(self,charName, dob, intell,sp):
        self.__CharacterName = charName
        self.__DateOfBirth = dob
        self.__Intelligence = intell
        self.__Speed = sp

#Q3aii
def GetIntelligence(self):
    return self.__Intelligence

def GetName(self):
    return self.__CharacterName

#Q3aiii
def GetIntelligence(self,newIntell):
    self.__Intelligence = newIntell

#Q3iv
def Learn(self):
    self.__Intelligence += self.__Intelligence * 0.1

#Q3av
def ReturnAge(self):
    age = 2023 - self.__DateOfBirth.year
    return age

#Q3bi
from datetime import datetime
FirstCharacter = Character("Royal",datetime(2019,1,1), 70, 30 )

#Q3bii
#FirstCharacter.Learn()
#print(f"Your character's name is {FirstCharacter.GetName()}, their age is {FirstCharacter.ReturnAge()} and their intelligence is{FirstCharacter.GetIntelligence()} ")

#Q3ci
class MagicCharacter(Character):
    def __init__(self,element,charName, dob, intell,sp):
        Character.__init__(charName, dob, intell,sp)
        self.__Element = element

#Q3cii
def Learn(self):
    Character.Learn()
    if self.__Element == 'fire' or self.__Element == 'water':
        self.__Intelligence += self.__Intelligence * 0.2
    elif self.__Element == 'earth':
        self.__Intelligence += self.__Intelligence * 0.3
    else:
        self.__Intelligence += self.__Intelligence * 0.1