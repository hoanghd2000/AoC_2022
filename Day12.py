from collections import deque
# Graph problem, shortest path from a src to a dst
def Day12a(file):
    # Process input
    file1 = open(file, 'r')
    map = file1.readlines()

    noRows, noCols = len(map), len(map[0]) - 1

    # BFS, to find shortest path
    def bfs(src, dst):
        q = deque() # A node in the queue should include: (r, c) coordinates, cost to reach that node
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Initialize
        q.append((src, 0))

        while q:
            cur, cur_cost = q.popleft()
            if cur not in visited:
                visited.add(cur)
                # print(cur)

                # If arrive at the dst
                if cur == dst:
                    return cur_cost
                
                # If have not arrived at the dst
                for dir in directions:
                    new_r, new_c = cur[0] + dir[0], cur[1] + dir[1]
                    if 0 <= new_r < noRows and 0 <= new_c < noCols:
                        if ord(map[new_r][new_c]) - ord(map[cur[0]][cur[1]]) <= 1 and (new_r, new_c) not in visited:
                            q.append(((new_r, new_c), cur_cost + 1))
        return None

    # Find the src and dst
    src = dst = None
    for r in range(noRows):
        for c in range(noCols):
            if map[r][c] == 'S':
                src = (r, c)
            if map[r][c] == 'E':
                dst = (r, c)
    
    # print(src, dst)
    map[src[0]] = map[src[0]].replace('S', 'a')
    map[dst[0]] = map[dst[0]].replace('E', 'z')
    # for line in map:
    #     print(line)
    res = bfs(src, dst)

    return res


def Day12b(file):
    # Process input
    file1 = open(file, 'r')
    map = file1.readlines()

    noRows, noCols = len(map), len(map[0]) - 1

    # BFS, to find shortest path
    def bfs(src, dst):
        q = deque() # A node in the queue should include: (r, c) coordinates, cost to reach that node
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Initialize
        q.append((src, 0))

        while q:
            cur, cur_cost = q.popleft()
            if cur not in visited:
                visited.add(cur)
                # print(cur)

                # If arrive at the dst
                if cur == dst:
                    return cur_cost
                
                # If have not arrived at the dst
                for dir in directions:
                    new_r, new_c = cur[0] + dir[0], cur[1] + dir[1]
                    if 0 <= new_r < noRows and 0 <= new_c < noCols:
                        if ord(map[new_r][new_c]) - ord(map[cur[0]][cur[1]]) <= 1 and (new_r, new_c) not in visited:
                            q.append(((new_r, new_c), cur_cost + 1))
        return None

    # Find the srcs and dst
    src = []
    dst = None
    for r in range(noRows):
        for c in range(noCols):
            if map[r][c] == 'a':
                src.append((r, c))
            if map[r][c] == 'S':
                map[r] = map[r].replace('S', 'a')
                src.append((r, c))
            if map[r][c] == 'E':
                dst = (r, c)
    map[dst[0]] = map[dst[0]].replace('E', 'z')

    # Result
    search_res = []
    for s in src:
        temp = bfs(s, dst)
        if temp:
            search_res.append(temp)
    return min(search_res)

if __name__ == "__main__":
    print("Day12a: ", Day12a("Day12.txt"))
    print("Day12b: ", Day12b("Day12.txt"))