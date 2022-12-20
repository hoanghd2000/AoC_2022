def Day10a(file):
    cur_cycle = 1 # ptr to keep track of what is the current cycle
    x = 1 # register X value

    # Read the file line by line
    file1 = open(file, 'r')
    lines = file1.readlines()

    signal_strength_sum = 0
    flag = [False] * 6

    # For each line, increment the cur_cycle and update the value of register X
    for line in lines:
        if "noop" in line:
            cur_cycle += 1
        elif "addx" in line:
            val = int(line.split()[-1])
            cur_cycle += 2
            x += val
        for milestone in range(20, 221, 40):
            if not flag[(milestone-20)//40] and cur_cycle in (milestone, milestone-1):
                #print(milestone, x)
                flag[(milestone-20)//40] = True
                signal_strength_sum += (x*milestone)
    
    return signal_strength_sum

def Day10b(file):
    x = 1 # register X value
    crt = [['.'] * 40 for i in range(6)] # crt
    file1 = open(file, 'r')

    # Flags
    cycle_count = 0
    val = 0

    # For each cycle
    for cycle in range(1, 241):
        # Draw the pixel for that cycle - CRT
        row, col = (cycle-1) // 40, (cycle-1) % 40 # row, col of the pixel being drawn in that cycle
        if x - 1 <= col <= x + 1:
            crt[row][col] = '#'
        else:
            crt[row][col] = '.'
        
        # Update the register X value, if applicable - CPU
        if cycle_count == 0:
            line = file1.readline()
            if "noop" in line:
                continue
            elif "addx" in line:
                cycle_count = 1
                val = int(line.split()[-1])
        elif cycle_count == 1:
            cycle_count -= 1
            x += val
    
    for r in range(6):
        for c in range(40):
            print(crt[r][c], end='')
        print()
    return crt

if __name__ == "__main__":
    print("Day10a: ", Day10a("Day10.txt"))
    Day10b("Day10.txt")