from collections import deque as queue
 
# Direction vectors for BFS traversal
dRow = [ -1, 1, 0, 0]
dCol = [ 0, 0, -1, 1]


def parse_input(input_data):
    """
    Parses input data string for barren land coordinates.
    Expects input in the format: {"x1 y1 x2 y2", "x1 y1 x2 y2", ...}
    where (x1, y1) is the bottom-left coordinate and (x2, y2) is the top-right coordinate.
    """
    while True:
        try:
            # Ensure the input data has curly braces and split by comma
            if not input_data.startswith('{"') or not input_data.endswith('"}'):
                raise ValueError("Input must start with '{' and end with '}'.")

            input_data = input_data[1:-1].split(",")

            barren_land = []
            for input_segment in input_data:
                # Strip leading/trailing whitespace and quotes, then split by space
                coordinates = input_segment.strip()[1:-1].split(" ")

                # Check if we have exactly 4 coordinates
                if len(coordinates) != 4:
                    raise ValueError("Each rectangle must have exactly 4 coordinates enclosed with double quotes and separated by a space.")

                # Convert strings to integers
                coordinates = tuple(map(int, coordinates))

                # Check if the coordinates are in the correct order
                if not (coordinates[0] <= coordinates[2] and coordinates[1] <= coordinates[3]):
                    raise ValueError("Coordinates must be in the form: x1 y1 x2 y2 where x1 <= x2 and y1 <= y2.")

                barren_land.append(coordinates)

            return barren_land

        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter the coordinates in the correct format for creating the barren rectangles.")
            print("Each rectangle is specified by 4 integers: {x1 y1 x2 y2}, where (x1, y1) is the bottom-left coordinate and (x2, y2) is the top-right coordinate.")
            print("Example: {\"0 292 399 307\", \"48 192 351 207\"}")
            input_data = input("Please provide the input again: ")


def create_grid(m,n):
    """
    created a grid with m rows and n columns
    and returns this created grid
    """
    grid  = [[1 for i in range(n)] for j in range(m)]
    return grid

def mark_barren_lands(grid, barren_land_coords):
    """
    Runs a FOR loop from the coordinates specified by a user and marks those rectangles as 0 indicating barren land
    """
    # print("mark barren lands function: ",barren_land_coords)
    for coord in barren_land_coords:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        # print(x1,y1, x2, y2)
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                grid[x][y] = 0 # mark as barren rectangle land
    # print(grid)
    # print("done")
    return grid

def BFS(grid, row, col,m,n):
    """
    Employs the Breadth First Search algorithm by creating a queue traversal
    where each queue coordinate is traversed in all 4 directions (left, right, up, down) 
    and then if the traversed direction is valid (within the grid) and not visited yet, adds the coordinates to the end of the queue
    Calculates the area of the visited block and then marks that as visited before the next iteration 
    """
    q = queue()

    q.append(( row, col ))
    area=0
    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        if(grid[x][y] ==1):
            area+=1
            grid[x][y] = -1 
            # Go to the adjacent cells
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                
                if ( (adjx >= 0 and  adjy >= 0 and adjx < m and adjy < n) ):
                    # print("adjx = ",adjx)
                    # print("adjy = ",adjy)
                    # print(m)
                    # print(n){"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}
                    # print("grid[",adjx,"][",adjy,"]")
                    if(grid[adjx][adjy] == 1):
                        q.append((adjx, adjy))                
    return area

def find_fertile_land(grid,m,n):
    """
    Iterates through the entire grid and creates area of each enclosed unvisited fertile land block by calling the BFS algorithm
    """
    area_list=[]
    for i in range(m):
        for j in range(n): 
            if(grid[i][j] == 1):
                area = BFS(grid, i, j,m,n)
                area_list.append(area)
    area_list.sort()
    print(area_list)
    return area_list

input_data = input("Provide the input of the barren land coordinates in a 400X600 m farm")
barren_land_coords = parse_input(input_data)
m=400 
n=600 
grid = create_grid(m,n)
mark_barren_lands(grid, barren_land_coords)
find_fertile_land(grid,m,n)

# Reference
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/
