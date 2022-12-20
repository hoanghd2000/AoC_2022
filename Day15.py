import re
def Day15a(file, target_row):
    # # Map
    # noRows, noCols = 5000000, 5000000
    # ground = [['.'] * noCols for i in range(noRows)]

    # For each sensor - beacon pair, mark the zone whereby no beacon could possibly be found
    # BETTER APPROACH: For each sensor - beacon pair, find the range of cells on target_row that cannot be the beacon
    def checkTargetRow(sensor_x, sensor_y, beacon_x, beacon_y):
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        vertical_dist = abs(sensor_y - target_row)
        max_horizontal_dist = dist - vertical_dist
        if max_horizontal_dist >= 0:
            left = sensor_x - max_horizontal_dist
            right = sensor_x + max_horizontal_dist
            if beacon_y == target_row:
                if beacon_x == left:
                    if beacon_x == right:
                        return []
                    else:
                        return [[left+1, right]]
                elif beacon_x == right:
                    return [[left, right-1]]
                else:
                    return [[left, right]]
            else:
                return [[left, right]]
        else:
            return []
    
    intervals = []
    file1 = open(file, 'r')
    lines = file1.readlines()
    for line in lines:
        m = re.match(r"Sensor at x=(?P<sensor_x>.+), y=(?P<sensor_y>.+): closest beacon is at x=(?P<beacon_x>.+), y=(?P<beacon_y>.+).*", line)
        sensor_x = int(m.groupdict()['sensor_x'])
        sensor_y = int(m.groupdict()['sensor_y'])
        beacon_x = int(m.groupdict()['beacon_x'])
        beacon_y = int(m.groupdict()['beacon_y'])
        # dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        # for r in range(dist+1):
        #     row = sensor_y + r
        #     for c in range(dist-r+1):
        #         col = sensor_x + c
        #         ground[row][col] = '#'
        #         col = sensor_x - c
        #         ground[row][col] = '#'
        #     row = sensor_y - r
        #     for c in range(dist-r+1):
        #         col = sensor_x + c
        #         ground[row][col] = '#'
        #         col = sensor_x - c
        #         ground[row][col] = '#'
        # ground[sensor_y][sensor_x] = 'S'
        # ground[beacon_y][beacon_x] = 'B'

        intervals.extend(checkTargetRow(sensor_x, sensor_y, beacon_x, beacon_y))

    # Merge overlapping intervals
    ## Sort the intervals based on starting positions
    intervals.sort(key=lambda a : a[0])
    #print(intervals)
    stack = []
    for interval in intervals:
        if stack:
            # if current interval overlaps with the interval on top of the stack
            if stack[-1][1] >= interval[0]:
                stack[-1][1] = max(interval[1], stack[-1][1])
            else: # else
                stack.append(interval)
        else:
            stack.append(interval)
    count = 0
    for interval in stack:
        #print(interval)
        count += (interval[1]-interval[0]+1)


    # Return the result
    # for cell in ground[target_row]:
    #     if cell == '#' or cell == 'S':
    #         count += 1
    return count


def Day15b(file, lower_b, upper_b):
    # # Map
    # noRows, noCols = 5000000, 5000000
    # ground = [['.'] * noCols for i in range(noRows)]

    def check1Row(file, target_row, lower_b, upper_b):
        # For each sensor - beacon pair, mark the zone whereby no beacon could possibly be found
        # BETTER APPROACH: For each sensor - beacon pair, find the range of cells on target_row that cannot be the beacon
        def checkTargetRow(sensor_x, sensor_y, beacon_x, beacon_y, target_row):
            dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            vertical_dist = abs(sensor_y - target_row)
            max_horizontal_dist = dist - vertical_dist
            if max_horizontal_dist >= 0:
                left = sensor_x - max_horizontal_dist
                right = sensor_x + max_horizontal_dist
                return [[left, right]]
            else:
                return []
        
        intervals = []
        file1 = open(file, 'r')
        lines = file1.readlines()
        for line in lines:
            m = re.match(r"Sensor at x=(?P<sensor_x>.+), y=(?P<sensor_y>.+): closest beacon is at x=(?P<beacon_x>.+), y=(?P<beacon_y>.+).*", line)
            sensor_x = int(m.groupdict()['sensor_x'])
            sensor_y = int(m.groupdict()['sensor_y'])
            beacon_x = int(m.groupdict()['beacon_x'])
            beacon_y = int(m.groupdict()['beacon_y'])
            # dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            # for r in range(dist+1):
            #     row = sensor_y + r
            #     for c in range(dist-r+1):
            #         col = sensor_x + c
            #         ground[row][col] = '#'
            #         col = sensor_x - c
            #         ground[row][col] = '#'
            #     row = sensor_y - r
            #     for c in range(dist-r+1):
            #         col = sensor_x + c
            #         ground[row][col] = '#'
            #         col = sensor_x - c
            #         ground[row][col] = '#'
            # ground[sensor_y][sensor_x] = 'S'
            # ground[beacon_y][beacon_x] = 'B'

            intervals.extend(checkTargetRow(sensor_x, sensor_y, beacon_x, beacon_y, target_row))

        # Merge overlapping intervals
        ## Sort the intervals based on starting positions
        intervals.sort(key=lambda a : a[0])
        #print(intervals)
        stack = []
        for interval in intervals:
            if stack:
                # if current interval overlaps with the interval on top of the stack
                if stack[-1][1] >= interval[0]:
                    stack[-1][1] = max(interval[1], stack[-1][1])
                else: # else
                    stack.append(interval)
            else:
                stack.append(interval)

        rangeindex_low, rangeindex_up = -1, -1
        for index, interval in enumerate(stack):
            if lower_b in range(interval[0], interval[1]+1):
                rangeindex_low = index
            if upper_b in range(interval[0], interval[1]+1):
                rangeindex_up = index
        #print("Row", target_row, ':', stack)
        if rangeindex_low == rangeindex_up:
            return False, 0
        return True, stack[rangeindex_low][1] + 1


    # Return the result
    # for cell in ground[target_row]:
    #     if cell == '#' or cell == 'S':
    #         count += 1
    # return count

    # For each possible row of the distress beacon, check if that row could contain the beacon
    for r in range(lower_b, upper_b+1):
        res = check1Row(file, r, lower_b, upper_b)
        if res[0]:
            print("x, y:", res[1], r)
            return res[1] * 4000000 + r

if __name__ == "__main__":
    print("Day15a: ", Day15a('Day15.txt', 2000000))
    print("Day15b: ", Day15b('Day15.txt', 0, 4000000))