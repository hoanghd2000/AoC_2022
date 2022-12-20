def Day14a(file):
    noRows = 200
    noCols = 1000
    map = [['.'] * noCols for i in range(noRows)]
    deepest = 0 # Keep track of the deepest col with rock
    sand_src = (0, 500) # The point where sand is pouring from

    # Populate the map with rocks
    file1 = open(file, 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.split(' -> ')
        for i in range(len(line)-1):
            start = line[i].split(',')
            end = line[i+1].split(',')
            start[0], start[1], end[0], end[1] = int(start[0]), int(start[1]), int(end[0]), int(end[1])
            deepest = max(deepest, start[1], end[1])
            if start[0] == end[0]:
                if start[1] <= end[1]:
                    for r in range(start[1], end[1]+1):
                        map[r][start[0]] = '#'
                else:
                    for r in range(end[1], start[1]+1):
                        map[r][start[0]] = '#'
            elif start[1] == end[1]:
                if start[0] <= end[0]:
                    for c in range(start[0], end[0]+1):
                        map[start[1]][c] = '#'
                else:
                    for c in range(end[0], start[0]+1):
                        map[start[1]][c] = '#'
    
    # Map printing
    for r in range(deepest+1):
        for c in range(490, 510):
            print(map[r][c], end='')
        print()

    # Simulate sand fall for 1 unit of sand
    ## Input: map before
    ## Output: where the unit of sand comes to rest
    ## Update map after the just introduced unit of sand comes to rest
    def sandfall():
        # Initialization
        sand_loc = sand_src # starting position of the sand
        directions = ((1, 0), (1, -1), (1, 1))
        
        while True:   # while new position of the sand could still be found, continue
            new_pos_found = False
            for dir in directions:
                new_r, new_c = sand_loc[0] + dir[0], sand_loc[1] + dir[1]
                if map[new_r][new_c] == '.':    # if a new position found
                    sand_loc = (new_r, new_c)
                    new_pos_found = True
                    break
            if not new_pos_found:   # The sand comes to rest
                map[sand_loc[0]][sand_loc[1]] = 'o'
                return sand_loc
            if new_r > deepest:     # The sand falls into the abyss
                return None
                
    count = 0
    rest_pos = sandfall()
    while rest_pos:
        count += 1
        rest_pos = sandfall()

    return count


def Day14b(file):
    noRows = 200
    noCols = 1000
    map = [['.'] * noCols for i in range(noRows)]
    deepest = 0 # Keep track of the deepest col with rock
    sand_src = (0, 500) # The point where sand is pouring from

    # Populate the map with rocks
    file1 = open(file, 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.split(' -> ')
        for i in range(len(line)-1):
            start = line[i].split(',')
            end = line[i+1].split(',')
            start[0], start[1], end[0], end[1] = int(start[0]), int(start[1]), int(end[0]), int(end[1])
            deepest = max(deepest, start[1], end[1])
            if start[0] == end[0]:
                if start[1] <= end[1]:
                    for r in range(start[1], end[1]+1):
                        map[r][start[0]] = '#'
                else:
                    for r in range(end[1], start[1]+1):
                        map[r][start[0]] = '#'
            elif start[1] == end[1]:
                if start[0] <= end[0]:
                    for c in range(start[0], end[0]+1):
                        map[start[1]][c] = '#'
                else:
                    for c in range(end[0], start[0]+1):
                        map[start[1]][c] = '#'
    # Populate the map with the floor
    for c in range(noCols):
        map[deepest + 2][c] = '#'
    
    # Map printing
    for r in range(deepest+1):
        for c in range(490, 510):
            print(map[r][c], end='')
        print()

    # Simulate sand fall for 1 unit of sand
    ## Input: map before
    ## Output: where the unit of sand comes to rest
    ## Update map after the just introduced unit of sand comes to rest
    def sandfall():
        # Initialization
        sand_loc = sand_src # starting position of the sand
        directions = ((1, 0), (1, -1), (1, 1))
        count = 0
        
        while True:   # while new position of the sand could still be found, continue
            new_pos_found = False
            for dir in directions:
                new_r, new_c = sand_loc[0] + dir[0], sand_loc[1] + dir[1]
                if map[new_r][new_c] == '.':    # if a new position found
                    sand_loc = (new_r, new_c)
                    new_pos_found = True
                    count += 1
                    break
            if not new_pos_found:   # The sand comes to rest
                if count == 0:
                    return None
                map[sand_loc[0]][sand_loc[1]] = 'o'
                return sand_loc
            # if new_r > deepest:     # The sand falls into the abyss
            #     return None
                
    count = 0
    rest_pos = sandfall()
    while rest_pos:
        count += 1
        rest_pos = sandfall()

    return count + 1


if __name__ == '__main__':
    print("Day14a: ", Day14a('Day14.txt'))
    print("Day14b: ", Day14b('Day14.txt'))