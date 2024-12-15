import pygame
import sys
import asyncio
from Grid import Grid

async def asyncPlay() -> None:
    pause = True
    moving = False
    
    grid = Grid(screen,resolution[1],resolution[0],size,spacing)
    grid.allocateLifes()
    grid.sendNeighbors()
    
    while True:
        screen.fill((50,50,50))
        grid.drawGrid()
        
        mx, my = pygame.mouse.get_pos()
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    moving = True
                    grid.click(mx,my)
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False    
            elif event.type == pygame.MOUSEMOTION and moving:
                grid.click(mx,my)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                if event.key == pygame.K_ESCAPE:
                    grid.clear()
                         
        pygame.display.update()
        
        if not pause:
            grid.callCheks()
            grid.nextState()
            clock.tick(10)
        else:   
            clock.tick(30)
            
        await asyncio.sleep(0)


    

if __name__ == "__main__":
    pygame.init()
    # Change this 3 parameters to control the look of the game 
    resolution = [720, 720] 
    size = 10
    spacing = 1
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((resolution[0], resolution[1]))

    asyncio.run(asyncPlay())