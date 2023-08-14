
# MY SOLUTION TO Bot_Building_1.py

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

    # for i in range(n):
    #     for j in range(n):
    #         if(grid[i][j]=='m'):
    #             bot_row = i
    #             bot_column = j
    #         if(grid[i][j]=='p'):
    #             princess_row = i
    #             princess_column = j

    for i in range(n):
        if 'm' in grid[i]:
            bot_row = i
            bot_column = grid[i].index('m')
        if 'p' in grid[i]:
            princess_row = i
            princess_column = grid[i].index('p')

    while(bot_column!=princess_column and bot_row!=princess_row):
        if(bot_row<princess_row):
            print("DOWN\n")
            bot_row+=1
        if(bot_row>princess_row):
            print("UP\n")
            bot_row-=1
        if(bot_column<princess_column):
            print("RIGHT\n")
            bot_column+=1
        if(bot_column>princess_column):
            print("LEFT\n")
            bot_column-=1
            

# m = int(input())
# grid = [] 
# mat =[]
# g=''
# k=0
# for i in range(0, m): 
#     grid.append(input().strip()) 
# for i in grid:
#     g = g+i  
# for i in range(m):
#     for j in range(m):
#         mat[i][j]= g[k]
#     k+=m
# print(mat)


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip()) 


displayPathtoPrincess(m,grid)