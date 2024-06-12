# Conway's Game of Life
Simple version of Conway's Game of Life made with python using pygame.
![Screenshot 2024-06-12 235402](https://github.com/memo1918/GameOfLife/assets/52012349/25b4d085-f892-4834-9c92-a6ba3e9c5324)


## Rules
A cell can be live or dead. Each cell interracts with its eight neighbors around.
At each step following rules apply:
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


## How to play
Game starts as paused. you can start and stop the game with "space" key.

Clicking on tiles places a live cell. You can also click and move the mouse to place along the way.

Pressing "ESC" clears the grid.

## How to run from source
- Download the code from the top right corner of github. Code -> Download ZIP
- Install python 3.11.4 if you don't have it already.
- Install pygame module. You can do it by running the command below on a terminal.
```cmd
pip install pygame
```
- Run main.py
```cmd
python src/main.py
```
Note: Make sure that all files are in the same folder

## Options
You can change the resolution and the size of the cells.
To do this, go to main.py and change these variables located at the bottom:
```python
resolution = [420,420] 
size = 10   # Size of the cells.
spacing = 1 # Size of the gap between cells.
```   
