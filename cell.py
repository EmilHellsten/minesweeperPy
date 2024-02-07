#The Cell tracks all the info related to a single cell on the board
class Cell:
  def __init__(self, col, row):#on initialization, pass in the coords from double loop to represent its column and row
    self.isMine = False
    self.isRevealed = False#initially, all cells on the board are untouched
    self.isFlagged = False#similarly, flags are placed by the player
    self.neighbouringMines = 0
    self.column = col
    self.row = row