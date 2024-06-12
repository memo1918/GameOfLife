class Life():
    def __init__(self, location:tuple[int,int], coordinates:tuple[int,int], state:bool) -> None:
        self.location = location
        self.coordinates = coordinates
        self.state = state
        self.neighs: list[Life] = []
        self.nextState: bool = False
        
    def checkState(self) -> None:
        num = 0
        for life in self.neighs:
            if life.state:
                num +=1
        
        if num == 3 and not self.state:
            self.nextState = True
        elif num < 2:
            self.nextState = False
        elif ((2<= num and num <=3) and self.state):
            self.nextState = True
        elif num > 3:
            self.nextState = False
            
                     
        
