from cell import Cell

class Board:
  def __init__(self, size, bombs):
    self.height = size
    self.width = size
    self.bombs = bombs#tää pois, tilalle funkkari joka muuttaa X määrän soluja pommeiks
    