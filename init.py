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
  height_curve = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ']
  width = 0
  width_curve = [' a ',' b ',' c ',' d ',' e ',' f ',' g ',' h ']

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
  def move_figure(self,start,finish):
    pass??
class Figure():
  x = 0
  y = 0
  rank = 0
  team = 0
  postion = 0
  value = " k "
  def __init__(self,b = Board.board,x = 0,y = 0,team = 0):
    self.team = team
    self.x = x
    self.y = y
    self.postion = converter(self.x,self.y)
    b[x][y] = change_value(self.value,self.team)
  def move():
    pass
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
    self.officers_init()
    self.queen_and_king()
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
  def officers_init(self):
    self.officers.append(Officer(x=0,y=2))
    self.officers.append(Officer(x=0,y=5))
    self.officers.append(Officer(x=7,y=2,team = 1))
    self.officers.append(Officer(x=7,y=5,team = 1))
  def queen_and_king(self):
    self.queen.append(Queen(x=0,y=3))
    self.king.append(King(x=0,y=4))
    self.queen.append(Queen(x=7,y=4,team=1))
    self.king.append(King(x=7,y=3,team=1))
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def converter(x,y):
  x+=1
  if (x < 0 or x > 7) or (y < 0 or y > 7):
    return 0
  d = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
  a = d[y] + str(x)
  return a
def reconverter(s):
  d = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
  s = list(s)
  x = get_key(d,s[0])
  y = (int(s[1]))
  return x,y
a = Board()
b = a.board
a.print_board()
p = Init()
a.print_board()
print(p.pawns[2].x,p.pawns[2].y)
print(p.pawns[15].postion)
