import sys, time
input = sys.stdin.read().split('\n')
# Visualizing Colors! =^.^=
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    # cancel SGR codes if we don't write to a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # set Windows console in VT mode
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32
# Visualizer Call to print the current state of the colors
def visualize(grid: list[list[bool]], condense:bool = True) -> None:
    toPrint = "\033[H"
    if not condense:
        for line in grid:
            for cell in line:
                toPrint += Colors.RED + '#' if cell else Colors.DARK_GRAY + '.'
                toPrint += Colors.END
            toPrint += '\n'
        print(toPrint)
        return
    newGrid = []
    for i in range(0, len(grid), 2):
        newLine = []
        for j in range(0, len(grid[0]), 2):
            cellSum = 0
            if grid[i][j]:
                cellSum += 1
            if grid[i+1][j]:
                cellSum += 1
            if grid[i][j+1]:
                cellSum += 1
            if grid[i+1][j+1]:
                cellSum += 1
            newLine.append(cellSum)
        newGrid.append(newLine)
    for line in newGrid:
        for cell in line:
            if cell == 0:
                toPrint += Colors.DARK_GRAY + '##' + Colors.END
            elif cell == 1:
                toPrint += Colors.LIGHT_GRAY + '##' + Colors.END
            elif cell == 2:
                toPrint += Colors.GREEN + '##' + Colors.END
            elif cell == 3:
                toPrint += Colors.RED + '##' + Colors.END
            elif cell == 4:
                toPrint += Colors.LIGHT_WHITE + '##' + Colors.END
        toPrint += '\n'
    print(toPrint, end='')
# Update a new version of the grid
def updateGrid(grid: list[list[bool]]) -> list[list[bool]]:
    newGrid = []
    for i in range(len(grid)):
        newLine = []
        for j in range(len(grid[0])):
            onNeighbors = 0
            if isNeighborOn(grid,i-1,j-1):
                onNeighbors += 1
            if isNeighborOn(grid,i-1,j):
                onNeighbors += 1
            if isNeighborOn(grid,i,j-1):
                onNeighbors += 1
            if isNeighborOn(grid,i+1,j-1):
                onNeighbors += 1
            if isNeighborOn(grid,i-1,j+1):
                onNeighbors += 1
            if isNeighborOn(grid,i+1,j):
                onNeighbors += 1
            if isNeighborOn(grid,i,j+1):
                onNeighbors += 1
            if isNeighborOn(grid,i+1,j+1):
                onNeighbors += 1
            if grid[i][j] and onNeighbors == 2 or onNeighbors == 3:
                newLine.append(True)
            elif not grid[i][j] and onNeighbors == 3:
                newLine.append(True)
            else:
                newLine.append(False)
        newGrid.append(newLine)
    newGrid[0][0] = True
    newGrid[len(grid)-1][0] = True
    newGrid[0][len(grid[0])-1] = True
    newGrid[len(grid)-1][len(grid[0])-1] = True
    return newGrid
#See if neighbor is real or not, and get value as needed
def isNeighborOn(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    return grid[i][j]
grid = []
for line in input:
    newLine = []
    for character in line:
        newLine.append(character == '#')
    grid.append(newLine)
grid[0][0] = True
grid[len(grid)-1][0] = True
grid[0][len(grid[0])-1] = True
grid[len(grid)-1][len(grid[0])-1] = True
isVis = True
steps = 100
if isVis:
    visualize(grid)
for i in range(steps):
    grid = updateGrid(grid)
    if isVis:
        time.sleep(0.2)
        visualize(grid)

count = 0
for i in grid:
    for j in i:
        if j:
            count += 1

print(count)