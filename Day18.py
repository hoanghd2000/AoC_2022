from collections import deque
def Day18a(file):
    cube_set = set()
    # Read the input
    file1 = open(file, 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.replace('\n', '')
        cube = line.split(',')
        cube = tuple(map(int, cube))
        cube_set.add(cube)
    
    # For a cube, count the sides that are uncovered.
    # Check for each of its side if it's covered, by checking if the cube that is supposed to cover that side is present
    def countOpenSides(x, y, z):
        count = 0
        if (x+1,y,z) in cube_set:
            count += 1
        if (x-1,y,z) in cube_set:
            count += 1
        if (x,y+1,z) in cube_set:
            count += 1
        if (x,y-1,z) in cube_set:
            count += 1
        if (x,y,z+1) in cube_set:
            count += 1
        if (x,y,z-1) in cube_set:
            count += 1
        return 6 - count

    # For each cube, countOpenSides, sum up to get total number of open sides
    numOpenSides = 0
    for cube in cube_set:
        numOpenSides += countOpenSides(cube[0], cube[1], cube[2])
    
    return numOpenSides



def Day18b(file):
    cube_set = set()
    # Read the input
    file1 = open(file, 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.replace('\n', '')
        cube = line.split(',')
        cube = tuple(map(int, cube))
        cube_set.add(cube)
    
    # For a cube, count the sides that are uncovered.
    # Check for each of its side if it's covered, by checking if the cube that is supposed to cover that side is present
    def countOpenSides(x, y, z):
        count = 0
        if (x+1,y,z) in cube_set or (x+1,y,z) in trapped_air_cubes_set:
            count += 1
        if (x-1,y,z) in cube_set or (x-1,y,z) in trapped_air_cubes_set:
            count += 1
        if (x,y+1,z) in cube_set or (x,y+1,z) in trapped_air_cubes_set:
            count += 1
        if (x,y-1,z) in cube_set or (x,y-1,z) in trapped_air_cubes_set:
            count += 1
        if (x,y,z+1) in cube_set or (x,y,z+1) in trapped_air_cubes_set:
            count += 1
        if (x,y,z-1) in cube_set or (x,y,z-1) in trapped_air_cubes_set:
            count += 1
        return 6 - count

    directions = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
    # Create a min 3-D cuboid within which the whole lava droplet lies and just touching the cuboid's faces
    max_x, max_y, max_z = 0, 0, 0
    for cube in cube_set:
        max_x = max(max_x, cube[0])
        max_y = max(max_y, cube[1])
        max_z = max(max_z, cube[2])
    max_x += 1
    max_y += 1
    max_z += 1
    
    # Flood fill (dfs) the part outside the lava droplet, within the cuboid
    q = deque()
    q.append((0, 0, 0))
    outside = set()
    while q:
        cur = q.pop()
        outside.add(cur)
        for dir in directions:
            new_x, new_y, new_z = cur[0] + dir[0], cur[1] + dir[1], cur[2] + dir[2]
            if 0 <= new_x <= max_x and 0 <= new_y <= max_y and 0 <= new_z <= max_z:
                if (new_x, new_y, new_z) not in outside and (new_x, new_y, new_z) not in cube_set:
                    q.append((new_x, new_y, new_z))
    
    # Flood fill (dfs) the part inside the lava droplet, yet also find trapped air cubes
    q = deque()
    start = cube_set.pop()
    q.append(start)
    cube_set.add(start)
    inside = set()
    trapped_air_cubes_set = set()
    while q:
        cur = q.pop()
        inside.add(cur)
        if cur not in cube_set:
            trapped_air_cubes_set.add(cur)
        for dir in directions:
            new_x, new_y, new_z = cur[0] + dir[0], cur[1] + dir[1], cur[2] + dir[2]
            if 0 <= new_x <= max_x and 0 <= new_y <= max_y and 0 <= new_z <= max_z:
                if (new_x, new_y, new_z) not in inside and (new_x, new_y, new_z) not in outside:
                    q.append((new_x, new_y, new_z))

    # For each cube, countOpenSides, sum up to get total number of open sides
    numOpenSides = 0
    for cube in cube_set:
        numOpenSides += countOpenSides(cube[0], cube[1], cube[2])
    return numOpenSides

if __name__ == "__main__":
    print("Day18a: ", Day18a('Day18.txt'))
    print("Day18b: ", Day18b('Day18.txt'))