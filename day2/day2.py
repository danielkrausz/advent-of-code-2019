import os
import sys

def main():
    fp = open(os.path.join(sys.path[0], 'day2.txt'), 'r')
    line = fp.readline().split(",")

    intcode = [int(num) for num in line]
    
    #Backup list
    intcode_reset = intcode.copy()

    #Replace initial positions
    intcode[1] = 12
    intcode[2] = 2

    run_intcode(intcode)

    #Day 2 - 1 star result
    print(f"Day 2 - 1 star result: {intcode[0]!s}")

    noun_verb = 0
    req_output = 19690720

    #Brute-force search
    for noun in range(100):
        for verb in range(100):
            intcode = intcode_reset.copy()
            intcode[1] = noun
            intcode[2] = verb
            run_intcode(intcode)
            if intcode[0] == req_output:
                noun_verb = noun * 100 + verb

    print(f"Day 2 - 2 star result: {noun_verb!s}")

def run_intcode(intcode):
    i = 0
    while intcode[i] != 99:
        if intcode[i] == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif intcode[i] == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        i += 4

if __name__ == "__main__":
    main()


