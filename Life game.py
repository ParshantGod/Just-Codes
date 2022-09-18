import random, time, copy

WIDTH = 60
HEIGHT= 20

#create a losyt of list foe the cells:
nextCells = []
for x in range (WIDTH):
    column = [] #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') # add a living cell
        else:
            column.append(' ')# Add a dead cell
    nextCells.append(column) # nextcells is a list of column lists.
while True: #main program loop
    print('\n\n\n\n\n') #separate each step with a new line
    currentCells = copy.deepcopy(nextCells)
    #print currentcells on the screen
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')#printthe # or space.
        print()
        
        # claculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighbouring coordinates:
            #% Width ensures leftcoor is alwats between 0 and WIDTH - 1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT
            
            #Count the number of living neighbours:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] =='#':
                numNeighbors +=1 #top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
                
            # setr cells based in conway's game of life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbours stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y]==' ' and numNeighbors == 3:
                #dead cells with 3 neighbrs become alive:
                nextCells[x][y] = '#'
            else:
                #Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1)
            
