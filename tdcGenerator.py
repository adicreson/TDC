from random import randint

class TdcGenerator:

    oldies = list({"Adam", "Axel", "Calle M", "Mathilda", "Anna", "Mirac", "Vilhelm", "Adi", "Tilde", "Stina", "Donja"})
    newbies = list({"Stella", "Morgan", "Riccardo", "Elin"})
    nbrOfRooms = 6

    def __init__(self):
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

    def createRoomPairings(self):
        parings = []
        roomsToCreate = self.nbrOfRooms
        while self.newbies:
            pass



    def createRoomOrder(self, pairings):
        pass
    
    def createTDC():
        pass

gen = TdcGenerator()

gen.testDistOldies(100000000)
#gen.testDistNewbies(100000) 

