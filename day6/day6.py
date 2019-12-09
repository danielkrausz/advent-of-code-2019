import os
import sys

def main():
    fp = open(os.path.join(sys.path[0], 'day6.txt'), 'r')

    lines = [line.rstrip('\n').split(')') for line in fp]

    obj_list = {}
    #Center of Mass
    obj_list["COM"] = None

    for line in lines:
        #Add parent to child - Every child has 1 parent
        obj_list[line[1]] = [line[0]]

    orbit_cnt = 0  

    #Day 6 - 1 star
    for key in obj_list:
        orbit_cnt += cnt_orbits(obj_list,key)

    print(f"Day 6 - 1 star: {orbit_cnt}")

    # DAY 6 - 2 star
    closest_common = common_parents(obj_list, "YOU", "SAN")[0]

    print(f"Day 6 - 2 star: {distance_to_obj(obj_list, 'YOU', closest_common) + distance_to_obj(obj_list, 'SAN', closest_common)}")

# Number of steps between an object and one of its parent (goal_obj)
def distance_to_obj(obj_list, key, goal_obj):
    return obj_list.get(key).index(goal_obj)


# List of common parent objects (direct & indirect) of two given objects
def common_parents(obj_list, you, san):
    common_items = []
    for i in obj_list.get(you):
        for j in obj_list.get(san):
            if i == j:
                common_items.append(i)

    return(common_items)


#Part 1 - Counting distance from obj to COM
def cnt_orbits(obj_list, obj_key):
    if obj_key != "COM":
            parent = obj_list.get(obj_key)[0]
    else:
        return 0
    
    orbit_cnt = 0

    while parent != None:
        orbit_cnt += 1
        if parent != "COM":
            # Adding all parents to list for part 2
            parent = obj_list.get(parent)[0]
            obj_list[obj_key].append(parent)
        else:
            break

    return orbit_cnt

if __name__ == "__main__":
    main()
