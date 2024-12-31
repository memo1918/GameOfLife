import pygame
import sys
import asyncio
from Grid import Grid

async def asyncPlay() -> None:
    pause = True
    moving = False
    
    grid = Grid(screen,resolution[1]-50,resolution[0],size,spacing)
    grid.allocateLifes()
    grid.sendNeighbors()
    
    leftButton = pygame.Rect(10,resolution[1]-50,resolution[0]/2-20,40)
    rightButton = pygame.Rect(resolution[0]/2+10,resolution[1]-50,resolution[0]/2-20,40)
    font = pygame.font.SysFont(None, 36)
    left_text = font.render('Clear', True, (255, 255, 255))
    right_text = font.render('Stop', True, (255, 255, 255))
    
    
    while True:
        screen.fill((50,50,50))
        grid.drawGrid()
        
        if pause:
            pygame.draw.rect(screen,"gray",rightButton)
        else:
            pygame.draw.rect(screen,"black",rightButton)
        
        pygame.draw.rect(screen,"black",leftButton)
        
        
        screen.blit(left_text, (leftButton.x + (leftButton.width - left_text.get_width()) // 2, leftButton.y + (leftButton.height - left_text.get_height()) // 2))
        screen.blit(right_text, (rightButton.x + (rightButton.width - right_text.get_width()) // 2, rightButton.y + (rightButton.height - right_text.get_height()) // 2))
        
        mx, my = pygame.mouse.get_pos()
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if leftButton.collidepoint(mx, my):
                        grid.clear()
                        continue
                    elif rightButton.collidepoint(mx, my):
                        pause = not pause
                        continue
                        
                    moving = True
                    grid.click(mx,my,True) 
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False    
            elif event.type == pygame.MOUSEMOTION and moving:
                grid.click(mx,my,False)
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
    resolution = [720, 770] 
    size = 10
    spacing = 1
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((resolution[0], resolution[1]))

    asyncio.run(asyncPlay())