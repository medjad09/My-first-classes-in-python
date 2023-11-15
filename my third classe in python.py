class Mobile():
    def __init__(self, number, companyName,name,storage, serialNum, dualSim, support4K):
        self.number = number
        self.companyName = companyName
        self.name = name
        self.storage = storage
        self.serialNum = serialNum
        self.dualSim = dualSim
        self.support4K = support4K

    def info(self):
        print("The phone {}, {}, the name is {}, the storage is {}GB, the serial number is {}, dual sim is {},support 4K {}".format(self.number, self.companyName, self.name, self.storage, self.serialNum, self.dualSim, self.support4K))

mobile1 = Mobile(1, "Samsung", "Galaxy S20", "256","265876965865", "Available", True)
mobile2 = Mobile(2, "Apple", "Iphone 13","256","366547886789" ,"Not Available" ,True)

mobile1.info()
mobile2.info()
