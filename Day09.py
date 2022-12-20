def Day9a(file):
    # Read the file line by line
    file1 = open(file, 'r')
    lines = file1.readlines()

    directions = { # Descartes coords
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

    # Check if H and T are touching
    def checkTouching(H, T):
        if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
            return True
        else:
            return False
    
    # Rules governing the motion
    # Fn to take input (H cur & pre position + T previous position), spit output (T cur position)
    def simulate(H_pre, H_move, T_pre):
        H_cur = (H_pre[0] + directions[H_move][0], H_pre[1] + directions[H_move][1])
        T_cur = None
        
        if checkTouching(H_cur, T_pre):
            return H_cur, T_pre
        else:
            if H_cur[0] - T_pre[0] == 2 and H_cur[1] == T_pre[1]:
                T_cur = (T_pre[0] + 1, T_pre[1])
            elif T_pre[0] - H_cur[0] == 2 and H_cur[1] == T_pre[1]:
                T_cur = (T_pre[0] - 1, T_pre[1])
            elif H_cur[1] - T_pre[1] == 2 and H_cur[0] == T_pre[0]:
                T_cur = (T_pre[0], T_pre[1] + 1)
            elif T_pre[1] - H_cur[1] == 2 and H_cur[0] == T_pre[0]:
                T_cur = (T_pre[0], T_pre[1] - 1)
            elif H_cur[0] != T_pre[0] and H_cur[1] != T_pre[1]:
                if H_cur[0] > T_pre[0] and H_cur[1] > T_pre[1]:
                    T_cur = (T_pre[0] + 1, T_pre[1] + 1)
                elif H_cur[0] > T_pre[0] and H_cur[1] < T_pre[1]:
                    T_cur = (T_pre[0] + 1, T_pre[1] - 1)
                elif H_cur[0] < T_pre[0] and H_cur[1] < T_pre[1]:
                    T_cur = (T_pre[0] - 1, T_pre[1] - 1)
                else:
                    T_cur = (T_pre[0] - 1, T_pre[1] + 1)
        
        return H_cur, T_cur
    
    # Process each line of the input
    H_pre = T_pre = (0, 0)  # Initialize
    T_pos_set = set()
    T_pos_set.add(T_pre)

    for line in lines:
        H_move, times = line.split()
        for time in range(int(times)):
            H_pre, T_pre = simulate(H_pre, H_move, T_pre)
            T_pos_set.add(T_pre)

    return len(T_pos_set)

def Day9b(file):
    # Read the file line by line
    file1 = open(file, 'r')
    lines = file1.readlines()

    directions = { # Descartes coords
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

    # Check if H and T are touching
    def checkTouching(H, T):
        if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
            return True
        else:
            return False

    
    # Rules governing the motion
    # Fn to take input (H pre position + H move + T previous position), spit output (H cur position + T cur position)
    def simulateHead(H_pre, H_move, T_pre):
        H_cur = (H_pre[0] + directions[H_move][0], H_pre[1] + directions[H_move][1])
        T_cur = None
        
        if checkTouching(H_cur, T_pre):
            return H_cur, T_pre
        else:
            if H_cur[0] - T_pre[0] == 2 and H_cur[1] == T_pre[1]:
                T_cur = (T_pre[0] + 1, T_pre[1])
            elif T_pre[0] - H_cur[0] == 2 and H_cur[1] == T_pre[1]:
                T_cur = (T_pre[0] - 1, T_pre[1])
            elif H_cur[1] - T_pre[1] == 2 and H_cur[0] == T_pre[0]:
                T_cur = (T_pre[0], T_pre[1] + 1)
            elif T_pre[1] - H_cur[1] == 2 and H_cur[0] == T_pre[0]:
                T_cur = (T_pre[0], T_pre[1] - 1)
            elif H_cur[0] != T_pre[0] and H_cur[1] != T_pre[1]:
                if H_cur[0] > T_pre[0] and H_cur[1] > T_pre[1]:
                    T_cur = (T_pre[0] + 1, T_pre[1] + 1)
                elif H_cur[0] > T_pre[0] and H_cur[1] < T_pre[1]:
                    T_cur = (T_pre[0] + 1, T_pre[1] - 1)
                elif H_cur[0] < T_pre[0] and H_cur[1] < T_pre[1]:
                    T_cur = (T_pre[0] - 1, T_pre[1] - 1)
                else:
                    T_cur = (T_pre[0] - 1, T_pre[1] + 1)
        
        return H_cur, T_cur
    
    # Rules governing the motion
    # Fn to take input (H cur position + T previous position), spit output (T cur position)
    def simulate(H_cur, T_pre):
        T_cur = None
        
        if checkTouching(H_cur, T_pre):
            return T_pre
        else:
            if H_cur[0] - T_pre[0] == 2 and H_cur[1] == T_pre[1]:
                T_cur = (T_pre[0] + 1, T_pre[1])
            elif T_pre[0] - H_cur[0] == 2 and H_cur[1] == T_pre[1]:
                T_cur = (T_pre[0] - 1, T_pre[1])
            elif H_cur[1] - T_pre[1] == 2 and H_cur[0] == T_pre[0]:
                T_cur = (T_pre[0], T_pre[1] + 1)
            elif T_pre[1] - H_cur[1] == 2 and H_cur[0] == T_pre[0]:
                T_cur = (T_pre[0], T_pre[1] - 1)
            elif H_cur[0] != T_pre[0] and H_cur[1] != T_pre[1]:
                if H_cur[0] > T_pre[0] and H_cur[1] > T_pre[1]:
                    T_cur = (T_pre[0] + 1, T_pre[1] + 1)
                elif H_cur[0] > T_pre[0] and H_cur[1] < T_pre[1]:
                    T_cur = (T_pre[0] + 1, T_pre[1] - 1)
                elif H_cur[0] < T_pre[0] and H_cur[1] < T_pre[1]:
                    T_cur = (T_pre[0] - 1, T_pre[1] - 1)
                else:
                    T_cur = (T_pre[0] - 1, T_pre[1] + 1)
        
        return T_cur
    
    # Process each line of the input
    H_pre = N1_pre = N2_pre = N3_pre = N4_pre = N5_pre = N6_pre = N7_pre = N8_pre = N9_pre = (0, 0)  # Initialize
    T_pos_set = set()
    T_pos_set.add(N9_pre)

    for line in lines:
        H_move, times = line.split()
        for time in range(int(times)):
            H_pre, N1_pre = simulateHead(H_pre, H_move, N1_pre)
            N2_pre = simulate(N1_pre, N2_pre)
            N3_pre = simulate(N2_pre, N3_pre)
            N4_pre = simulate(N3_pre, N4_pre)
            N5_pre = simulate(N4_pre, N5_pre)
            N6_pre = simulate(N5_pre, N6_pre)
            N7_pre = simulate(N6_pre, N7_pre)
            N8_pre = simulate(N7_pre, N8_pre)
            N9_pre = simulate(N8_pre, N9_pre)
            T_pos_set.add(N9_pre)

    return len(T_pos_set)

if __name__ == "__main__":
    print("Day9a: ", Day9a("Day9.txt"))
    print("Day9b: ", Day9b("Day9.txt"))