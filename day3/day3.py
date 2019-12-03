import os
import sys
import numpy

cols = 25000
rows = 10000
start_x = 2000
start_y = 2000

dist_list = []
cross_set_2 = []
cross_set_1 = []

cross_size_sum = []

path = numpy.zeros((rows, cols))

def main():
    fp = open(os.path.join(sys.path[0], 'day3.txt'), 'r')

    wire_1 = fp.readline().strip('\n').split(',')
    wire_2 = fp.readline().split(',')

    fp.close()

    #Day 3 - 1 star
    calc_path(wire_1, 1)
    calc_path(wire_2, 2)

    print(f"Day 3 - 1 star result: {sorted(dist_list)[1]}")

    #Day 3 - 2 star
    calc_path(wire_1, 3)

    #Summarize intersection req. steps
    for coord1 in cross_set_1:
        for coord2 in cross_set_2:
            if (coord1[0] == coord2[0] and coord1[1] == coord2[1]):
                cross_size_sum.append(coord1[2] + coord2[2])

    print(f"Day 3 - 2 star result: {sorted(cross_size_sum)[1]}")

def calc_path(wire, idx):
    pos = [start_x, start_y]
    step_count = 0
    for cmd in wire:
        direction = cmd[:1]
        dist = cmd[1:]
        for step in range(0, int(dist)):
            if idx == 1:
                path[pos[0], pos[1]] = 1
            elif idx == 2:
                if path[pos[0], pos[1]] == 1.0:
                    path[pos[0], pos[1]] = 2
                    dist_list.append(man_dist(start_x, start_y, pos[0], pos[1]))
                    cross_set_2.append((pos[0], pos[1], step_count))
            elif idx == 3:
                if path[pos[0], pos[1]] == 2.0:
                    cross_set_1.append((pos[0], pos[1], step_count))
                
            if direction == 'U':
                pos[0] += 1
            elif direction == 'L':
                pos[1] -= 1
            elif direction == 'R':
                pos[1] += 1
            elif direction == 'D':
                pos[0] -= 1

            step_count+=1

def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main()