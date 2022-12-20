def Day8a(file):
    # Read all lines of the file
    file1 = open(file, 'r')
    lines = file1.readlines()
    # print(lines)

    noRows, noCols = len(lines), len(lines[0])-1

    # 2-D grid to keep track of tree visibility
    vis = [[0] * noCols for x in range(noRows)]

    def checkVis(r, c, vis, inc):
        vis[r][c] = 1
        tallest_height = int(lines[r][c])
        new_r, new_c = r + inc[0], c + inc[1]
        while 0 <= new_r < noRows and 0 <= new_c < noCols:
            if int(lines[new_r][new_c]) > tallest_height:
                vis[new_r][new_c] = 1
                tallest_height = int(lines[new_r][new_c])
            new_r, new_c = new_r + inc[0], new_c + inc[1]
    
    # Check along rows and cols from the trees at the edges to see which trees are visible
    for c in range(noCols):
        checkVis(0, c, vis, (1, 0))
        checkVis(noRows - 1, c, vis, (-1, 0))
    for r in range(noRows):
        checkVis(r, 0, vis, (0, 1))
        checkVis(r, noCols - 1, vis, (0, -1))
    # for line in vis:
    #     print(line)

    return sum(map(sum, vis))

def Day8b(file):
    # Read the file line by line
    file1 = open(file, 'r')
    lines = file1.readlines()

    noRows, noCols = len(lines), len(lines[0])-1

    def calScenicScore(r, c):
        # Fn to count tree seen along a straight line in a given dir
        def countSeenTree(r, c, dir):
            count = 0
            new_r, new_c = r + dir[0], c + dir[1]
            while 0 <= new_r < noRows and 0 <= new_c < noCols:
                count += 1
                if int(lines[new_r][new_c]) >= int(lines[r][c]):
                    break
                new_r, new_c = new_r + dir[0], new_c + dir[1]
            return count
        
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        score = 1
        for dir in directions:
            score *= countSeenTree(r, c, dir)
        return score

    highest_scenic_score = 0
    for r in range(noRows):
        for c in range(noCols):
            highest_scenic_score = max(highest_scenic_score, calScenicScore(r, c))
    
    return highest_scenic_score

if __name__ == "__main__":
    print("Day8a: ", Day8a("Day8.txt"))
    print("Day8b: ", Day8b("Day8.txt"))