import math

def Day11a(file):
    monkey_items = []
    operation = []
    test = []
    destination = []
    inspection_count = []
    file1 = open(file, 'r')
    lines = file1.readlines()
    cur_monkey = None

    # Process the input
    for line in lines:
        if "Monkey" in line:
            monkey_items.append([])
            inspection_count.append(0)
            cur_monkey = int(line.split()[1][0])
        elif "Starting items:" in line:
            for item in line.split(':')[1].split(','):
                monkey_items[cur_monkey].append(int(item.strip()))
        elif "Operation:" in line:
            rhs = line.split("=")[1].split()
            if rhs[2] == 'old':
                if rhs[1] == '+':
                    operation.append([lambda a, val : a + a, 0])
                elif rhs[1] == '*':
                    operation.append([lambda a, val : a * a, 0])
            else:
                val = int(rhs[2])
                if rhs[1] == '+':
                    operation.append([lambda a, val : a + val, val])
                elif rhs[1] == '-':
                    operation.append([lambda a, val : a - val, val])
                elif rhs[1] == '*':
                    operation.append([lambda a, val : a * val, val])
                elif rhs[1] == '/':
                    operation.append([lambda a, val : a // val, val])
        elif "Test:" in line:
            divisor = int(line.split()[-1])
            test.append([lambda a, divisor: a % divisor, divisor])
        elif "If true:" in line:
            destination.append([])
            destination[-1].append(int(line.split()[-1]))
        elif "If false:" in line:
            destination[-1].append(int(line.split()[-1]))
                
    # Simulate monkey business for 20 rounds
    for i in range(20):
        # 1-round of monkey business
        for monkey in range(len(operation)):
            # print(monkey_items[monkey])
            count = 0 # Tracker for number of times each monkey inspect items
            # A monkey inspects all items one-by-one
            while monkey_items[monkey]:
                item = monkey_items[monkey].pop(0)
                item = operation[monkey][0](item, operation[monkey][1]) // 3
                count += 1
                # Monkey test item's worry level
                if test[monkey][0](item, test[monkey][1]) == 0:
                    monkey_items[destination[monkey][0]].append(item)
                else:
                    monkey_items[destination[monkey][1]].append(item)
            inspection_count[monkey] += count
    
    inspection_count.sort(reverse=True)
    return (inspection_count[0] * inspection_count[1])


def Day11b(file):
    monkey_items = []
    operation = []
    test = []
    destination = []
    inspection_count = []
    file1 = open(file, 'r')
    lines = file1.readlines()
    cur_monkey = None

    # Process the input
    for line in lines:
        if "Monkey" in line:
            monkey_items.append([])
            inspection_count.append(0)
            cur_monkey = int(line.split()[1][0])
        elif "Starting items:" in line:
            for item in line.split(':')[1].split(','):
                monkey_items[cur_monkey].append(int(item.strip()))
        elif "Operation:" in line:
            rhs = line.split("=")[1].split()
            if rhs[2] == 'old':
                if rhs[1] == '+':
                    operation.append([lambda a, val : a + a, 0])
                elif rhs[1] == '*':
                    operation.append([lambda a, val : a * a, 0])
            else:
                val = int(rhs[2])
                if rhs[1] == '+':
                    operation.append([lambda a, val : a + val, val])
                elif rhs[1] == '-':
                    operation.append([lambda a, val : a - val, val])
                elif rhs[1] == '*':
                    operation.append([lambda a, val : a * val, val])
                elif rhs[1] == '/':
                    operation.append([lambda a, val : a // val, val])
        elif "Test:" in line:
            divisor = int(line.split()[-1])
            test.append([lambda a, divisor: a % divisor, divisor])
        elif "If true:" in line:
            destination.append([])
            destination[-1].append(int(line.split()[-1]))
        elif "If false:" in line:
            destination[-1].append(int(line.split()[-1]))
    
    # Hash_num to reduce worry level
    hash_num = math.prod(list(zip(*test))[1])

    # Simulate monkey business for 10000 rounds
    for i in range(10000):
        # 1-round of monkey business
        for monkey in range(len(operation)):
            # print(monkey_items[monkey])
            count = 0 # Tracker for number of times each monkey inspect items
            # A monkey inspects all items one-by-one
            while monkey_items[monkey]:
                item = monkey_items[monkey].pop(0)
                item = operation[monkey][0](item, operation[monkey][1])
                count += 1
                # Monkey test item's worry level
                if test[monkey][0](item, test[monkey][1]) == 0:
                    next_monkey = destination[monkey][0]
                    monkey_items[next_monkey].append(item % hash_num)
                else:
                    next_monkey = destination[monkey][1]
                    monkey_items[next_monkey].append(item % hash_num)
            inspection_count[monkey] += count
    
    # Result
    inspection_count.sort(reverse=True)
    return (inspection_count[0] * inspection_count[1])


if __name__ == "__main__":
    print("Day11a: ", Day11a("Day11.txt"))
    print("Day11b: ", Day11b("Day11.txt"))