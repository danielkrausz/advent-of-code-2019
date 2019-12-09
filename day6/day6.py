import os
import sys

def main():
    fp = open(os.path.join(sys.path[0], 'day6.txt'), 'r')
    # line = fp.readline().strip('\n').split(')')

    lines = [line.rstrip('\n').split(')') for line in fp]

    obj_list = {}
    obj_list["COM"] = None

    for line in lines:
        #Add parent to child - Every child has 1 parent
        obj_list[line[1]] = line[0]

    orbit_cnt = 0  

    for key in obj_list:
        orbit_cnt += cnt_orbits(obj_list,key)
        
    print(orbit_cnt)
    
#Part 1 - Counting distance from obj to *COM*
def cnt_orbits(obj_list, obj_key):
    parent = obj_list.get(obj_key)
    orbit_cnt = 0

    while parent != None:
        orbit_cnt += 1 
        parent = obj_list.get(parent)

    return orbit_cnt

if __name__ == "__main__":
    main()
