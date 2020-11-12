from square import Square

class Board:

    """
    Square [] board: array with all the squares
    Piece [] pieces: all the pieces in the board
    """


    def __init__ (self):
        #Creates a 8x8 matrix of squares
        self.board = []
        for x in range(0,8):
            row = []
            for y in range (0,8):
                sq = Square([x,y])
                row.append(sq)  

            self.board.append(row)     
        # End of board creation
                
    def addPiece(self, piece, position):
        return None

    def removePiece(self, piece, position):
        return None

    def printBoard(self):
        out=""
        for row in self.board:
            for square in row:
                out+=str(square.getColor())
                
            out+="\n"
        print (out)
