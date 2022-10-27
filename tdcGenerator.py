from random import randint
from xml.dom.pulldom import parseString

class TdcGenerator:
    oldies = list({"Adam", "Axel", "Calle M", "Mathilda", "Anna", "Mirac", "Vilhelm", "Adi", "Tilde", "Stina", "Donja"})
    #oldies = list({"Adam", "Axel", "Calle M", "Mathilda"})
    newbies = list({"Stella", "Morgan", "Riccardo", "Elin"})
    nbrOfRooms = 6
    nbrOfParticipants = len(oldies) + len(newbies)

    def __init__(self):
        pass

    #Randomly selects a random oldie from oldies
    def __randomOldie(self):
        randOldIdx = randint(0, len(self.oldies) - 1)
        randOldie = self.oldies.pop(randOldIdx)
        return randOldie

    #Randomly selects a random newbie from newbies
    def __randomNewbie(self):
        randNewbIdx = randint(0, len(self.newbies) - 1)
        randNewbie = self.newbies.pop(randNewbIdx)
        return randNewbie

    def createRoomPairings(self):
        #Assert guarantees that there are enough participants to create at least pairings of two for number of chosen rooms
        assert self.nbrOfParticipants >= self.nbrOfRooms*2, "Too few participants to create room pairings of two"
        pairings = []
        roomsLeftToCreate = self.nbrOfRooms

        if len(self.oldies) >= len(self.newbies):
            #Start by creating pairs of newbies and oldies.
            while self.newbies:
                randNewbie = self.__randomNewbie()
                randOldie = self.__randomOldie()

                pairing = [randNewbie, randOldie]
                pairings.append(pairing)

                roomsLeftToCreate -= 1
            #If there are still oldies left after creating pairs of newbies and oldies, create pairs of oldies.
            while self.oldies:
                if roomsLeftToCreate != 0:
                    randOldie1 = self.__randomOldie()
                    randOldie2 = self.__randomOldie()

                    pairing = [randOldie1, randOldie2]
                    pairings.append(pairing)

                    roomsLeftToCreate -= 1
                else:
                    #If there are still oldies left after all pairs of two have been created, assign them randomly to the already created pairings.
                    #Needs correction to ensure that the randOldies get evenly distributed
                    while self.oldies:
                        assert len(pairings) == self.nbrOfRooms, "Error in code. There should be an equal amount of pairings and number of rooms"
                        randOldie = self.__randomOldie()
                        pairIdx = randint(0, len(pairings) - 1)
                        pairings[pairIdx].append(randOldie)


        pairings.sort(key = len)
        for pairing in pairings:
            print(pairing)
                    
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
            dist[element] = dist.get(element, 0) + 1 #edundant to use get, since all values are set to 0.

        for key, value in dist.items():
                percDist[key] = value/n

        theoDist = 1/(len(list))
        sum = 0
        print("Theoretical distribution: {:.3f}%".format(theoDist*100))
        print("----------------------------")
        for key, value in percDist.items():
            print("{} : {:.3f}%".format(key, value*100))
            sum += value
        print("----------------------------")
        print("Sum: {:.3f}%".format(sum*100))


    def testDistOldies(self, n):
        self.__testDistribution(self.oldies, n)
    
    def testDistNewbies(self, n):
        self.__testDistribution(self.newbies, n)

gen = TdcGenerator()

#gen.createRoomPairings()
gen.testDistOldies(1000)
#gen.testDistNewbies(10000) 

