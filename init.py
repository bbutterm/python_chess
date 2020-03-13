#len 1-8, heigh a-h
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
class Pawn(Figure):
  rank = 1
  team = 0
  value = " p "
  

a = Board()
b = a.board
a.print_board()
p = Pawn(b,x = 1,y = 1,team = 1)
a.print_board()
f = change_value("jopa",1)
print(f)
