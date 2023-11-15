class Car():
    def __init__(self, number,mark, model, nitroSpeed, color, speed):
        self.number = number
        self.mark = mark
        self.model = model
        self.nitroSpeed = nitroSpeed
        self.color = color
        self.speed = speed

    def info(self):
        print("The car number {}, {}, model is {}, nitro speed is {}, color is {}".format(self.number, self.mark, self.model, self.nitroSpeed, self.speed, self.color))

player1 = Car(1, "Ford", "Fiesta", "Not available","188/h", "Gray")
player2 = Car(2, "Opel", "Crossland x","Turbo D","178/h" ,"White")

player1.info()
player2.info()
