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
    
    I = {x: 1<<i for i, x in enumerate(flow_dict)}
    T = {x: {y: 1 if y in adj_list[x] else float('+inf') for y in adj_list} for x in adj_list}
    for k in T:
        for i in T:
            for j in T:
                T[i][j] = min(T[i][j], T[i][k]+T[k][j])

    # Simulate all possible scenarios for the whole process duration
    answer = {}
    q = collections.deque() # each node represents the current state, consists of minute_left, cur_valve, pressure_released (by end of that min), open_valves
    q.append((30, start_valve, 0, 0))
    while q:
        cur = q.popleft()
        # print(cur)
        minute_left, cur_valve, pressure_released, open_valves = cur
        answer[open_valves] = max(answer.get(open_valves, 0), pressure_released)
        # Else, move to another valve and open it
        for next_valve in adj_list:
            if flow_dict[next_valve] > 0 and (I[next_valve] & open_valves) == 0: # If there is still at least 1 unopened valve
                # cost = bfs(cur_valve, next_valve)
                cost = T[cur_valve][next_valve] + 1
                if minute_left <= cost:
                    continue
                # Update total pressure released
                ## If next move exceed duration
                new_pressure_released = pressure_released + flow_dict[next_valve] * (minute_left-cost)
                next_state = (minute_left-cost, next_valve, new_pressure_released, I[next_valve] | open_valves)
                q.append(next_state)

    return max(answer.values())

if __name__ == "__main__":
    print("Day16a: ", Day16a('Day16.txt'))
    # print("Day16b: ", Day16b('Day16.txt'))