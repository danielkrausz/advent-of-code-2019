import os
import sys

def main():
    fp = open(os.path.join(sys.path[0], 'day5.txt'), 'r')
    line = fp.readline().split(",")

    intcode = [int(num) for num in line]
    
    #Backup list
    intcode_reset = intcode.copy()

    run_intcode(intcode)

def run_intcode(intcode):
    i = 0
    while intcode[i] != 99:
        param = str(intcode[i]).rjust(5, 0)
        if param[-2:] == '01':
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
            i += 4
        elif param[-2:] == '02':
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
            i += 4
        elif param[-2:] == '03':
            intcode[intcode[i]] == input()
            i += 2
        elif intcode[i] == '04':
            intcode[intcode[i]]

if __name__ == "__main__":
    main()


