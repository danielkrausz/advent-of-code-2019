import os
import sys
import numpy

cols = 25000
rows = 10000
start_x = 2000
start_y = 2000

dist_list = []
path = numpy.zeros((rows, cols))

def main():
    fp = open(os.path.join(sys.path[0], 'day3.txt'), 'r')

    wire_1 = fp.readline().strip('\n').split(',')
    wire_2 = fp.readline().split(',')

    fp.close()

    path_1 = calc_path(wire_1, 1)
    path_2 = calc_path(wire_2, 2)
    path_sum = numpy.add(path_1, path_2)

    # numpy.set_printoptions(threshold=sys.maxsize)

    # print(path_1)
    # print(path_2)
    # print(path_sum)

    # for x in range(0, rows):
    #     for y in range(0, cols):
    #         if path_sum[x][y] == 2:
    #             dist_list.append(man_dist(start_x, start_y, x, y))

    dist_list.sort()
    print(dist_list[1])

def calc_path(wire, idx):
    pos = [start_x, start_y]
    for cmd in wire:
        direction = cmd[:1]
        dist = cmd[1:]
        for step in range(0, int(dist)):
            # print(pos)
            if idx == 1:
                path[pos[0], pos[1]] = 1
            elif idx == 2:
                if path[pos[0], pos[1]] == 1.0:
                    dist_list.append(man_dist(start_x, start_y, pos[0], pos[1]))
            if direction == 'U':
                pos[0] += 1
            elif direction == 'L':
                pos[1] -= 1
            elif direction == 'R':
                pos[1] += 1
            elif direction == 'D':
                pos[0] -= 1
    return(path)

def man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main()