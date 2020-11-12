class Square:

    """
    int [] position: position in the board (x,y)
    int color: 0=black 1=white
    boolean ocuppied: checks if the square has a piece on it or not
    """

    def __init__(self, position):
        self.position=position
        self.__setColor()
        self.ocuppied = False

    def getOcupation(self):
        return self.ocuppied

    def setOcupation(self, ocuppied):
        self.ocuppied = ocuppied

    def getPosition(self):
        return self.position

    def __setColor(self):
        p = self.position[0]  + self.position[1]
        if (p%2) == 0:
            self.color = 1
        else:
            self.color = 0

    def getColor(self):
        return self.color

    def toString(self):
        if self.color == 0:
            color = "negro"
        else:
            color = "blanco"

        return f"[{self.position[0]},{self.position[1]}] = {color}"
    
