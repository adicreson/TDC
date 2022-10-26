from random import randint

class TdcGenerator:

    oldies = list({"Adam", "Axel", "Calle M", "Mathilda", "Anna", "Mirac", "Vilhelm", "Adi", "Tilde", "Stina", "Donja"})
    newbies = list({"Stella", "Morgan", "Riccardo", "Elin"})

    def __init__(self):
        pass

    def __testDistribution(self, list, n):
        dist = {}
        percDist = {}
        

        for i in range(n):
            randIndex = randint(0, len(list) - 1)
            element = list[randIndex]
            dist[element] = dist.get(element, 0) + 1
        
        for key, value in dist.items():
                percDist[key] = value/n

        theoDist = 1/(len(list))
        print("Theoretical distribution: {}".format(theoDist))
        for key, value in percDist.items():
            print("{} : {}".format(key, value))

    def testDistOldies(self, n):
        self.__testDistribution(self.oldies, n)
    
    def testDistNewbies(self, n):
        self.__testDistribution(self.newbies, n)

    def createRoomPairings(self):
        parings = []
        

    def createRoomOrder(self, pairings):
        pass
    
    def createTDC():
        pass

gen = TdcGenerator()

gen.testDistOldies(5)
gen.testDistNewbies(100000) 

