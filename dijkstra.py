matrix = [[0, 6, 6, ], [6, 5, 2, ], [3, 9, 5]]

def path_finder(matrix):
    #defining length
    length = len(matrix)
    #defining start
    start = (0,0)
    #parameters
    final = (length - 1,length - 1)

    #store visited nodes, init start node(same for cost)
    visited = {start: 0}
    cost = {start: 0}

    #memoization
    frontier = [start]
    #while loop keep algorithm running
    while frontier:
        x,y = frontier.pop()
        if (x,y) == final:
            return matrix[x][y] + cost[(x,y)]

        parent_x, parent_y = x,y

        #cardinal directions
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):

            #to avoid out of range index
            if 0 <= x < length and 0 <= y < length:
                weight = cost[(parent_x, parent_y)] + matrix[x][y]


                #if stuck, at wall
                if (x,y) not in visited or weight < cost[(x,y)]:
                    frontier.append((x,y))
                    visited[(x,y)] = (parent_x, parent_y)
                    cost[(x,y)] = weight
    return False

print(path_finder(matrix))
# got help from Anish
#https://www.youtube.com/watch?v=FSm1zybd0Tk
