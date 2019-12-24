from itertools import permutations

#inputProgram = list(map(int,input().split(",")))
#hardcoded input
inputProgram = [3,8,1005,8,329,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,29,2,1102,1,10,1,1009,16,10,2,4,4,10,1,9,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,66,2,106,7,10,1006,0,49,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,95,1006,0,93,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,120,1006,0,61,2,1108,19,10,2,1003,2,10,1006,0,99,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,157,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,179,2,1108,11,10,1,1102,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,209,2,108,20,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,234,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,256,2,1102,1,10,1006,0,69,2,108,6,10,2,4,13,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,294,1,1107,9,10,1006,0,87,2,1006,8,10,2,1001,16,10,101,1,9,9,1007,9,997,10,1005,10,15,99,109,651,104,0,104,1,21101,387395195796,0,1,21101,346,0,0,1105,1,450,21101,0,48210129704,1,21101,0,357,0,1105,1,450,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,46413147328,1,21102,404,1,0,1106,0,450,21102,179355823323,1,1,21101,415,0,0,1105,1,450,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,838345843476,1,21101,0,438,0,1105,1,450,21101,709475709716,0,1,21101,449,0,0,1105,1,450,99,109,2,22102,1,-1,1,21102,40,1,2,21101,0,481,3,21101,0,471,0,1105,1,514,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,476,477,492,4,0,1001,476,1,476,108,4,476,10,1006,10,508,1101,0,0,476,109,-2,2106,0,0,0,109,4,2101,0,-1,513,1207,-3,0,10,1006,10,531,21101,0,0,-3,21201,-3,0,1,21201,-2,0,2,21101,1,0,3,21101,550,0,0,1105,1,555,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,578,2207,-4,-2,10,1006,10,578,21201,-4,0,-4,1105,1,646,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,597,0,0,1105,1,555,22102,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,616,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,638,22102,1,-1,1,21101,638,0,0,106,0,513,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

#defines
memorySize = 2000
class pixel:
  def __init__(self, color):
    self.color = color
    self.painted = 0

  def paint(self, color):
    if color != self.color:
      self.painted = 1
    self.color = color 

  def __repr__(self):
    return str(self.color)

class painter:
  def __init__(self, width, lenght, x, y):
    self.width = width
    self.lenght = lenght
    self.x = x
    self.y = y
    self.board = list ()
    self.orient = 1 #1 up 2 right 3 down 4 left
    for i in range(lenght):
      self.board.append(list())
      for j in range(width):
        self.board[-1].append(pixel(0))

  def getPainted(self):
    painted = 0
    for i in range(self.lenght):
      for j in range(self.width):
        painted += self.board[i][j].painted
    return painted
        
  def process(self, paint, turn):
    #paint
    self.board[self.y][self.x].paint(paint)

    #turn
    if turn == 0:
      self.orient -= 1
      if self.orient == 0:
        self.orient = 4
    if turn == 1:
      self.orient += 1
      if self.orient == 5:
        self.orient = 1

    #move
    if self.orient == 1:
      self.y -= 1
    if self.orient == 2:
      self.x += 1
    if self.orient == 3:
      self.y += 1
    if self.orient == 4:
      self.x -= 1

    #output
    return self.board[self.y][self.x].color
    


class compu:
  def __init__(self, prog, inp):
    global memorySize
    self.program = list(prog)
    self.inputBuffer = list(inp)
    self.outputBuffer = list()
    self.state = 1 #1=new, 2=ended, 3=paused
    self.itr = 0
    self.relativeBase = 0
    while len(self.program) < memorySize:
      self.program.append(0)

  def addInput(self, inp):
    self.inputBuffer.extend(inp)

  def parseCode(self, code):
    p3 = int(code / 10000)
    code = code % 10000
    p2 = int(code / 1000)
    code = code % 1000
    p1 = int(code / 100)
    code = code % 100
    return p1, p2, p3, code

  #parse and process opcode
  def processCode(self, itr):
    code = self.program[itr]
    p1, p2, p3, code = self.parseCode(code)
    if code == 99:
      return "quit"

    # process code
    # 1 parameter
    if p1 == 1:
      ind1 = itr+1
    elif p1 == 2:
      ind1 = self.program[itr+1] + self.relativeBase
    else:
      ind1 = self.program[itr+1]
  
    if code == 3:
      if not self.inputBuffer:
        return "pause"
      self.program[ind1] = self.inputBuffer.pop(0)
      return 2

    if code == 4:
      self.outputBuffer.append(self.program[ind1])
      return 2

    if code == 9:
      self.relativeBase += self.program[ind1]
      return 2
    # 2 parameters  
    if p2 == 1:
      ind2 = itr+2
    elif p2 == 2:
      ind2 = self.program[itr+2] + self.relativeBase
    else:
      ind2 = self.program[itr+2]
    if code == 5:
      if self.program[ind1] != 0:
        return self.program[ind2] - itr
      else:
        return 3
    if code == 6:
      if self.program[ind1] == 0:
        return self.program[ind2] - itr
      else:
        return 3 
    # 3 parameters  
    if p3 == 1:
      ind3 = itr+3
    elif p3 == 2:
      ind3 = self.program[itr+3] + self.relativeBase
    else:
      ind3 = self.program[itr+3]
    if code == 1:
      self.program[ind3] = self.program[ind1] + self.program[ind2]
      return 4
    if code == 2:
      self.program[ind3] = self.program[ind1] * self.program[ind2]
      return 4
    if code == 7:
      if self.program[ind1] < self.program[ind2]:
        self.program[ind3] = 1
        return 4
      self.program[ind3] = 0
      return 4
    if code == 8:
      if self.program[ind1] == self.program[ind2]:
        self.program[ind3] = 1
        return 4
      self.program[ind3] = 0
      return 4

    print("BAD CODE:")
    print(str(code))
    return "quit"

  # prepere and process program
  def ProcessProgram(self):
    #prep program
    self.outputBuffer.clear()
    move = 0
    process = True
    #process program
    while process:
      move = self.processCode(self.itr)
      if move == "quit":
        self.state = 2
        self.itr = 0
        process = False
      elif move == "pause":
        self.state = 3
        process = False
      else :
        self.itr += move
    return self.state, self.outputBuffer



# main
pri = painter(1500,1500,300,300)
buf = [0]
com = compu(inputProgram,[0])
state = com.state
instructs = 0
while state != 2:
  state, ret = com.ProcessProgram()
  print(ret)
  buf = [pri.process(ret[0],ret[1])]
  com.addInput(buf)
  instructs += 1
print(pri.getPainted())
print(instructs)