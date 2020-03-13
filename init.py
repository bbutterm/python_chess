#len 1-8, heigh a-h
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
def print_line(list):
  s = ""
  for i in list:
    s+=i
  print(s)
a = Board()
j = 0
for i in a.board:
  print_line(i)
  j+=1
print_line(a.width_curve)
