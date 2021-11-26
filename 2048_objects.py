class Board
    def __init__(self):
        self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

class Game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False

    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()

    def link_keys(self,event):
        if self.end or self.won:
            return

    self.gamepanel.compress = False
    self.gamepanel.merge = False
    self.gamepanel.moved = False

    self.gamepanel.paintGrid()
    print(self.gamepanel.score)

    flag=0
    for i in range(4):
        for j in range(4):
            if(self.gamepanel.gridCell[i][j]==0:
                flag=1
                break
            


