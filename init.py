#len 1-8, heigh a-h
#additional functions
def change_value(value,team):
  s = ""
  if team == 0:
    s +=value
  else:
    s += '\033[96m'
    s += value
    s += '\033[0m'
  return (s)
def print_line(list):
  s = ""
  for i in list:
    s+=i
  print(s)

class Board():
  board = []
  height = 0
  height_curve = ['a','b','c','d','e','f','g','h']
  width = 0
  width_curve = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ']

  def __init__(self,size=10):
    for i in range(1,9):
      self.board.append([])
    for i in self.board:
      for j in range(1,9):
        i.append("|_|")
    j = 0
    for i in self.height_curve:
      self.board[j].append(i)
      j+=1
  def print_board(self):
    for i in self.board:
      print_line(i)
    print_line(a.width_curve)
class Figure():
  x = 0
  y = 0
  rank = 0
  team = 0
  value = " k "
  def __init__(self,b = Board.board,x = 0,y = 0,team = 0):
    self.team = team
    self.x = x
    self.y = y
    b[x][y] = change_value(self.value,self.team)
  def info(self):
    print(self.x," ",self.y)
    print("rank = ", self.rank)

class Pawn(Figure):
  rank = 1
  value = "|p|"
class Horse(Figure):
  rank = 2
  value = "|h|"
class Tower(Figure):
  rank = 3
  value = "|t|"
class Officer(Figure):
  rank = 4
  value = "|o|"
class Queen(Figure):
  rank = 5
  value = "|q|"
class King(Figure):
  rank = 0
  value = "|k|"
class Init():
  pawns = []
  horses = []
  towers = []
  officers = []
  queen = []
  king = []
  #pawns[0] = white
  #pawns[1] = black
  def __init__(self):
    self.pawns_init()
    self.towers_init()
    self.horses_init()
  def pawns_init(self):
    i = 0
    while (i < 8):
      self.pawns.append(Pawn(x=1, y=i, team=0))
      i += 1
    i = 0
    while (i < 8):
      self.pawns.append(Pawn(x=6, y=i, team=1))
      i += 1
  def towers_init(self):
    self.towers.append(Tower(x=0, y=0, team=0))
    self.towers.append(Tower(x=0, y=7, team=0))
    self.towers.append(Tower(x=7, y=0, team=1))
    self.towers.append(Tower(x=7, y=7, team=1))
  def horses_init(self):
    self.horses.append(Horse(x=0, y=1, team=0))
    self.horses.append(Horse(x=0, y=6, team=0))
    self.horses.append(Horse(x=7, y=1, team=1))
    self.horses.append(Horse(x=7, y=6, team=1))

a = Board()
b = a.board
a.print_board()
p = Init()
a.print_board()
