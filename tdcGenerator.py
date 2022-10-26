from random import randint
from xml.dom.pulldom import parseString

class TdcGenerator:

    oldies = list({"Adam", "Axel", "Calle M", "Mathilda", "Anna", "Mirac", "Vilhelm", "Adi", "Tilde", "Stina", "Donja"})
    newbies = list({"Stella", "Morgan", "Riccardo", "Elin"})
    nbrOfRooms = 6
    nbrOfParticipants = len(oldies) + len(newbies)

    def __init__(self):
        pass

    #Randomly selects a random Oldie from oldies
    def __randomOldie(self):
        randOldIdx = randint(0, len(self.oldies) - 1)
        randOldie = self.oldies.pop(randOldIdx)
        return oldie

    #Randomly selects a random Oldie from newbies
    def __randomNewbie(self):
        randNewbIdx = randint(0, len(self.newbies) - 1)
        newbie = self.newbies.pop(randNewbIdx)
        return newbie

    def createRoomPairings(self):
        #Assert guarantees that there are enough participants to create at least pairings of two for number of chosen rooms
        assert self.nbrOfParticipants >= self.nbrOfRooms*2, "Too few participants to create room pairings of two"
        pairings = []
        roomsLeftToCreate = self.nbrOfRooms

        if len(self.oldies) >= len(self.newbies):
            while self.newbies:
                newbie = self.__randomNewbie()
                oldie = self.__randomOldie()

                pairing = [newbie, oldie]
                pairings.append(pairing)

                roomsLeftToCreate -= 1

            while self.oldies:
                if roomsLeftToCreate != 0:
                    oldie1 = self.__randomOldie()
                    oldie2 = self.__randomOldie()

                    pairing = [oldie1, oldie2]
                    pairings.append[pairing]

                    roomsLeftToCreate -= 1
                else:
                    assert len(pairings) == self.nbrOfRooms, "Error in code. There should be an equal amount of pairings and number of rooms"
                    
                    PairIdx = randint(0, len(pairings) - 1)
                    pairings[]
                    



        return pairings                
            

    def createRoomOrder(self, pairings):
        pass
    
    def createTDC():
        pass

    def __testDistribution(self, list, n):
        dist = {}
        percDist = {}
        
        for key in list:
            dist[key] =  0
            
        for i in range(n):
            randIndex = randint(0, len(list) - 1)
            element = list[randIndex]
            dist[element] = dist.get(element, 0) + 1 ##Redundand to use get, since all values are set to 0.

        for key, value in dist.items():
                percDist[key] = value/n

        theoDist = 1/(len(list))
        print("Theoretical distribution: {:.4f}".format(theoDist))
        for key, value in percDist.items():
            print("{} : {:.4f}".format(key, value))

    def testDistOldies(self, n):
        self.__testDistribution(self.oldies, n)
    
    def testDistNewbies(self, n):
        self.__testDistribution(self.newbies, n)

gen = TdcGenerator()


gen.createRoomOrder()
#gen.testDistOldies(100000)
#gen.testDistNewbies(100000) 

