from random import randint

class TdcGenerator:
    #Different lists for testing
    #oldies = list({"Oldie1"})
    oldies = list({"Oldie1", "Oldie2", "Oldie3", "Oldie4", "Oldie5"})
    #oldies = list({"Oldie1", "Oldie2", "Oldie3", "Oldie4", "Oldie5", "Oldie6", "Oldie7", "Oldie8", "Oldie9", "Oldie10"})
    #newbies = list({"Newbie1"})
    newbies = list({"Newbie1", "Newbie2", "Newbie3", "Newbie4", "Newbie5"})
    #newbies = list({"Newbie1", "Newbie2", "Newbie3", "Newbie4", "Newbie5", "Newbie6", "Newbie7", "Newbie8", "Newbie9", "Newbie10"})

    nbrOfRooms = 5
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
    
    #Creates random room pairings based on the critera that newbies and oldies should be assigned together
    def __createRoomPairings(self):
        #Assert guarantees that there are enough participants to create at least pairings of two for number of chosen rooms
        assert self.nbrOfParticipants >= self.nbrOfRooms*2, "Too few participants to create room pairings of two"
        pairings = []
        roomsLeftToCreate = self.nbrOfRooms

            
        while self.newbies and self.oldies and roomsLeftToCreate > 0: 
            randNewbie = self.__randomNewbie()
            randOldie = self.__randomOldie()

            pairing = [randNewbie, randOldie]
            pairings.append(pairing)

            roomsLeftToCreate -= 1

        #While there are still oldies left after creating pairs of newbies and oldies and there are rooms left to create, create pairs of oldies.
        while self.oldies and roomsLeftToCreate > 0: #The assert above guarantees that there are atleast two people left if there are rooms left to create.
            randOldie1 = self.__randomOldie()
            randOldie2 = self.__randomOldie()

            pairing = [randOldie1, randOldie2]
            pairings.append(pairing)

            roomsLeftToCreate -= 1
        
        #While there are still newbies left after creating pairs of newbies and oldies, and there are rooms left to create, create pairs of newbies.
        while self.newbies and roomsLeftToCreate: #The assert above guarantees that there are atleast two people left if there are rooms left to create.
            randNewbie1 = self.__randomNewbie()
            randNewbie2 = self.__randomNewbie()

            pairing = [randNewbie1, randNewbie2]
            pairings.append(pairing)

            roomsLeftToCreate -= 1

        assignments = 0
        tmp = pairings.copy()
        #While there are still oldies left after all pairs of two and all rooms have been created, assign them randomly, but evenly, to the already created pairings.
        while self.oldies:
            assert len(pairings) == self.nbrOfRooms, "Error in code. There should be an equal amount of pairings: {} and number of rooms {}".format(len(pairings), self.nbrOfRooms)
            randOldie = self.__randomOldie()
            if assignments % len(pairings) == 0:
                tmp = pairings.copy()
            
            pairIdx = randint(0, len(tmp) - 1)
            tmp.pop(pairIdx).append(randOldie)
            assignments += 1

        #While there are still newbies left after all pairs of two and rooms have been created, assign them randomly, but evenly, to the already created pairings.
        while self.newbies:
            assert len(pairings) == self.nbrOfRooms, "Error in code. There should be an equal amount of pairings: {} and number of rooms: {}".format(len(pairings), self.nbrOfRooms)
            randNewbie = self.__randomNewbie()
            if assignments % len(pairings)  == 0:
                tmp = pairings.copy()
            
            pairIdx = randint(0, len(tmp) - 1)
            tmp.pop(pairIdx).append(randNewbie)
            assignments += 1        
        
        pairings.sort(key = len)
        #for pairing in pairings:
        #    print(pairing)
        
        return pairings               
            
    #Creates random room order based on the randomly created room pairings
    def __createRoomOrder(self):
        pairings = self.__createRoomPairings()
        roomOrder = []

        for roomNbr in range(1, len(pairings) + 1):
            pairIdx = randint(0, len(pairings) -1)
            pair = pairings.pop(pairIdx)
            roomOrder.append((roomNbr, pair))

        return roomOrder
    
    def createTDC(self):
        roomOrder = self.__createRoomOrder()
        
        print("*These are the randomly assigned rooms based on the criteria that oldies and newbies should be assigned together")
        print("*The room ordering has also been randomly assigned")
        print("------------------------------")
        for  tuple in roomOrder:
            roomNbr, pair = tuple
            print("Room {}: \t{}".format(roomNbr, pair))
        print("------------------------------")
    
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

gen.createTDC()

