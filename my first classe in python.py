class Player():
    def __init__(self, number,name, rank, age):
        self.number = number
        self.name = name
        self.rank = rank
        self.age = age

    def info(self):
        print("The player number {}, {}, rank is {}, age is {}".format(self.number, self.name, self.rank, self.age))

player1 = Player(1, "Ali", 5, 22)
player2 = Player(2, "Anas", 8, 32)

player1.info()
player2.info()
