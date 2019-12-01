import math
import os
import sys

def main():
    fp = open(os.path.join(sys.path[0], 'day1.txt'), 'r')
    sum = 0
    sum_all_modules = 0
    line = fp.readline()

    while line:
        sum += calc_fuel(int(line))
        sum_all_modules += calc_fuel_fuel(int(line), 0)
        line = fp.readline()


    fp.close()
    #Day1 - 1 star result
    print(f"Day 1 - 1 star solution: {sum!s}")
    #Day1 - 2 star result
    print(f"Day 1 - 2 star solution: {sum_all_modules!s}")
    

def calc_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel

def calc_fuel_fuel(mass, module_sum):
    if calc_fuel(mass) <= 0:
        return module_sum

    else:
        return calc_fuel_fuel(calc_fuel(mass), module_sum + calc_fuel(mass))

if __name__ == "__main__":
    main()
