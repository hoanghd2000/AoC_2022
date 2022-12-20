from functools import cmp_to_key
from math import prod
def Day13a(file):
    # To process data
    def processInput(line):
        # To keep track of the packet data
        stack = []
        ptr = 0

        while ptr < len(line):
            if line[ptr] == '[':
                stack.append('[')
                ptr += 1
            elif line[ptr] == ']':
                list1 = []
                cur = stack.pop()
                while cur != '[':
                    list1.append(cur)
                    cur = stack.pop()
                list1.reverse()
                stack.append(list1)
                ptr += 1
            elif line[ptr] == ',' or line[ptr] == '\n':
                ptr += 1
            else:
                start_ptr = ptr
                while line[ptr].isnumeric(): # account for multi-digit numbers
                    ptr += 1
                stack.append(int(line[start_ptr:ptr]))
        
        if len(stack) == 1:
            return stack[0]
        else:
            return "Error!"

    # Rules/logic for the order of the packages
    def isInRightOrd(left, right):
        # if both values are integers
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif right < left:
                return -1
            else:
                return 0
        
        # if exactly 1 is an int
        if isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]

        # if both values are lists
        l, r = iter(left), iter(right)
        while True:
            try:
                next_l, next_r = next(l), next(r)
                res = isInRightOrd(next_l, next_r)
                if res == 1 or res == -1:
                    return res
            except StopIteration:
                break
                
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0


    file1 = open(file, 'r')
    line1 = file1.readline()
    line2 = file1.readline()
    index = 1
    index_sum = 0
    indexes = []
    while line1 and line2:
        line1 = processInput(line1)
        line2 = processInput(line2)
        res = isInRightOrd(line1, line2)
        if res == 1:
            index_sum += index
            indexes.append(index)
        
        # Read the next pair of input
        file1.readline()
        line1 = file1.readline()
        line2 = file1.readline()
        index += 1
    #print(indexes)
    return index_sum

def Day13b(file):
    # To process data
    def processInput(line):
        # To keep track of the packet data
        stack = []
        ptr = 0

        while ptr < len(line):
            if line[ptr] == '[':
                stack.append('[')
                ptr += 1
            elif line[ptr] == ']':
                list1 = []
                cur = stack.pop()
                while cur != '[':
                    list1.append(cur)
                    cur = stack.pop()
                list1.reverse()
                stack.append(list1)
                ptr += 1
            elif line[ptr] == ',' or line[ptr] == '\n':
                ptr += 1
            else:
                start_ptr = ptr
                while line[ptr].isnumeric(): # account for multi-digit numbers
                    ptr += 1
                stack.append(int(line[start_ptr:ptr]))
        
        if len(stack) == 1:
            return stack[0]
        else:
            return "Error!"

    # Rules/logic for the order of the packages
    def isInRightOrd(left, right):
        # if both values are integers
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif right < left:
                return -1
            else:
                return 0
        
        # if exactly 1 is an int
        if isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]

        # if both values are lists
        l, r = iter(left), iter(right)
        while True:
            try:
                next_l, next_r = next(l), next(r)
                res = isInRightOrd(next_l, next_r)
                if res == 1 or res == -1:
                    return res
            except StopIteration:
                break
                
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0


    file1 = open(file, 'r')
    line1 = file1.readline()
    lines = []
    while line1:
        if line1 != '\n':
            lines.append(processInput(line1))
        line1 = file1.readline()
    lines.append([[2]])
    lines.append([[6]])
    lines = sorted(lines, key=cmp_to_key(isInRightOrd), reverse=True) # sort the packets
    return prod(i for i, k in enumerate(lines, 1) if k in [[[2]], [[6]]])


if __name__ == "__main__":
    print("Day13a: ", Day13a("Day13.txt"))
    print("Day13b: ", Day13b("Day13.txt"))