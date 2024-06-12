from pygame import draw, Rect
from Life import Life
class Grid():
    def __init__(self,screen ,height:int, width:int, gridSize:int, spacing:int) -> None:
        self.screen = screen
        self.height = height
        self.width = width
        self.gridSize = gridSize
        self.spacing = spacing
        self.lifes: list[list[Life]] = []
        
    def calculateGrid(self) -> list:
        wSize = int(self.width/(self.gridSize+self.spacing))
        hsize = int(self.height/(self.gridSize+self.spacing))
        
        coordinates = []
        for w in range(wSize):
            for h in range(hsize):
                coordinates.append((w*(self.gridSize+self.spacing), h*(self.gridSize+self.spacing)))

        return coordinates
    
    def allocateLifes(self) -> None:
        coordinates = self.calculateGrid() 
        
        hsize = int(self.height/(self.gridSize+self.spacing))
        
        for j,coordinate in enumerate(coordinates):
            if j% hsize==0:
                self.lifes.append([])
                
            self.lifes[-1].append(Life((coordinate[0]//(self.gridSize+self.spacing), coordinate[1]//(self.gridSize+self.spacing)),
                                       (coordinate[0],coordinate[1]),False))


    def drawGrid(self) -> None:
        for rows in self.lifes:
            for life in rows:                
                block = Rect(life.coordinates[0], life.coordinates[1], self.gridSize, self.gridSize)
                if life.state:
                    draw.rect(self.screen,"white",block)
                else:
                    draw.rect(self.screen,"black",block)
            
    def click(self,mx,my) -> None:
        y = my//(self.gridSize+self.spacing)
        x = mx//(self.gridSize+self.spacing)
        try: 
            clicked =  self.lifes[x][y]
            clicked.state = True
        except:
            return


    
    def sendNeighbors(self) -> None:
        for row in self.lifes:
            for life in row:
                x,y = life.location[0],life.location[1]
                neighbors = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
                
                for neigh in neighbors:
                    if neigh[0] < 0 or neigh[1] < 0:
                        continue
                    try:
                        temp = self.lifes[neigh[0]][neigh[1]]
                        life.neighs.append(temp)
                    except:
                        continue
    
    def callCheks(self) -> None:
        for row in self.lifes:
            for life in row:
                life.checkState()

    def nextState(self) -> None:
        for row in self.lifes:
            for life in row:
                life.state = life.nextState
                
    def clear(self) -> None:
        for row in self.lifes:
            for life in row:
                life.state = False
                life.nextState = False
        

        
        
        