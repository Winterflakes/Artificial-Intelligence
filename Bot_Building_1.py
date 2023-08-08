# Hackerrank

# Bot saves princess

# Princess Peach is trapped in one of the four corners of a square grid. 
# You are in the center of the grid and can move one step at a time in any of the four directions. 
# Can you rescue the princess?

# Input format

# The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. 
# This is followed by an NxN grid. 
# Each cell is denoted by '-' (ascii value: 45). 
# The bot position is denoted by 'm' and the princess position is denoted by 'p'.
# Grid is indexed using Matrix Convention

# Output format

# Print out the moves you will take to rescue the princess in one go. 
# The moves must be separated by '\n', a newline. 
# The valid moves are LEFT or RIGHT or UP or DOWN.


def displayPathtoPrincess(n,grid):

    princess = []
    bot = []
    for k,i in enumerate(grid): 

        # enumerate assigns a number to each element and 
        # if its (grid,100) numbering starts from 100
        # default is 0

        if "p" in i:
            princess = [i.index("p"),k]
        if "m" in i:
            bot = [i.index("m"),k]

        # It iterates through each row (i) of the grid using enumerate(grid) 
        # to find the positions of the princess and the bot. 
        # When it finds "p" in a row, it stores the row index (k) and 
        # the index of "p" in that row as the position of the princess. 
        # Similarly, when it finds "m" in a row, it stores the row index (k) and
        # the index of "m" in that row as the position of the bot
            
    x = princess[0] - bot[0]
    y = princess[1] - bot[1]
    if x > 0:
        for i in range(x):
            print("RIGHT")
    if x < 0:
        for i in range(-1*x):
            print("LEFT")
    if y > 0:
        for i in range(y):
            print("DOWN")
    if y < 0:
        for i in range(-1*y):
            print("UP")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip()) 
    
    # The strip() method removes any leading, and trailing whitespaces
    # specific element can also be romoved if not whitespaces
    
displayPathtoPrincess(m,grid)