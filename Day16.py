import re, collections
import sys
# Graph problem
def Day16a(file):
    # Process the input, produce a adj list and flow dict
    start_valve = "AA"
    end_minute = 30
    adj_list = {}
    flow_dict = {}
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        m = re.match(r"Valve (?P<valve_name>\w+) has flow rate=(?P<flow_rate>\w+); tunnels* leads* to valves* (?P<neighbours>.+)(\n)*", line)
        adj_list[m.groupdict()['valve_name']] = m.groupdict()['neighbours'].split(', ')
        flow_dict[m.groupdict()['valve_name']] = int(m.groupdict()['flow_rate'])
    
    # # Test
    # print(flow_dict)
    T = {x: {y: 1 if y in adj_list[x] else float('+inf') for y in adj_list} for x in adj_list}
    for k in T:
        for i in T:
            for j in T:
                T[i][j] = min(T[i][j], T[i][k]+T[k][j])

    def bfs(src, dst):
        q = collections.deque()
        q.append((src, 0))
        visited = set()

        while q:
            cur = q.popleft()
            cur_valve, cur_cost = cur
            visited.add(cur_valve)
            if cur_valve == dst:
                return cur_cost
            for neighbour in adj_list[cur_valve]:
                if neighbour not in visited:
                    q.append((neighbour, cur_cost + 1))
        return None

    # Simulate all possible scenarios for the whole process duration
    most_pressuree_released = 0
    visited = []
    q = collections.deque() # each node represents the current state, consists of minute, cur_valve, pressure_released (by end of that min), open_valves
    q.append((0, start_valve, 0, []))
    while q:
        cur = q.popleft()
        if cur in visited:
            continue
        visited.append(cur)
        # print(cur)
        cur_minute, cur_valve, pressure_released, open_valves = cur

        # # Test
        # if cur_minute < 10:
        #     print(cur)

        if cur_minute == end_minute:    # terminal state
            if pressure_released > most_pressuree_released:
                most_pressuree_released = pressure_released
        else:
            # Check if cur_valve is open. If not, can open it if its flow rate > 0
            if cur_valve not in open_valves and flow_dict[cur_valve] > 0:
                # Update total pressure released
                new_pressure_released = pressure_released
                for open_valve in open_valves:
                    new_pressure_released = new_pressure_released + flow_dict[open_valve]
                next_state = (cur_minute + 1, cur_valve, new_pressure_released, list(open_valves) + [cur_valve])
                if next_state not in q and next_state not in visited:
                    # temp = open_valves + [cur_valve]
                    # if temp[:4] == ['DD', 'BB', 'JJ', 'HH']:
                    #     print(cur)
                    #     print(next_state)
                    #     print(remaining)
                    #     print((new_pressure_released-pressure_released)/remaining)
                    # elif temp[:3] == ['DD', 'BB', 'JJ']:
                    #     print(cur)
                    #     print(next_state)
                    #     print(remaining)
                    #     print((new_pressure_released-pressure_released)/remaining)
                    # elif temp[:2] == ['DD', 'BB']:
                    #     print(cur)
                    #     print(next_state)
                    #     print(remaining)
                    #     print((new_pressure_released-pressure_released)/remaining)
                    # elif temp[:1] == ['DD']:
                    #     print(cur)
                    #     print(next_state)
                    #     print(remaining)
                    #     print((new_pressure_released-pressure_released)/remaining)
                    q.append(next_state)
            # Else, move to another valve instead of opening the current valve
            else:
                next_valve_found = False
                for next_valve in adj_list:
                    if next_valve not in open_valves and flow_dict[next_valve] > 0: # If there is still at least 1 unopened valve
                        next_valve_found = True
                        # cost = bfs(cur_valve, next_valve)
                        cost = T[cur_valve][next_valve]
                        # Update total pressure released
                        remaining = cost
                        ## If next move exceed duration
                        if cur_minute + cost > end_minute:
                            remaining = end_minute - cur_minute
                            next_valve = cur_valve
                        new_pressure_released = pressure_released
                        for open_valve in open_valves:
                            new_pressure_released = new_pressure_released + (remaining * flow_dict[open_valve])
                        next_state = (cur_minute + remaining, next_valve, new_pressure_released, list(open_valves))
                        if next_state not in q and next_state not in visited:
                            # if open_valves[:4] == ['DD', 'BB', 'JJ', 'HH']:
                            #     print(cur)
                            #     print(next_state)
                            #     print(remaining)
                            #     print((new_pressure_released-pressure_released)/remaining)
                            q.append(next_state)
                if not next_valve_found: # If there is no more unopened valve
                    remaining = end_minute - cur_minute
                    new_pressure_released = pressure_released
                    for open_valve in open_valves:
                        new_pressure_released = new_pressure_released + (remaining * flow_dict[open_valve])
                    next_state = (end_minute, cur_valve, new_pressure_released, list(open_valves))
                    if next_state not in q and next_state not in visited:
                        # if open_valves[:4] == ['DD', 'BB', 'JJ', 'HH']:
                        #     print(cur)
                        #     print(next_state)
                        #     print(remaining)
                        #     print((new_pressure_released-pressure_released)/remaining)
                        q.append(next_state)

    return most_pressuree_released

if __name__ == "__main__":
    print("Day16a: ", Day16a('Day16.txt'))
    # print("Day16b: ", Day16b('Day16.txt'))