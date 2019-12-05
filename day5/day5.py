import os
import sys

def main():
    fp = open(os.path.join(sys.path[0], 'day5.txt'), 'r')
    line = fp.readline().split(",")

    intcode = [int(num) for num in line]
    
    #Backup list
    intcode_copy = intcode.copy()

    #Day 5 - part 1
    run_intcode(intcode, 1)
    #Day 5 - part 2
    run_intcode(intcode_copy, 5)

def run_intcode(intcode, input_id):
    i = 0
    while str(intcode[i])[-2:] != '99':
        param = str(intcode[i]).rjust(5, '0')
        opcode = param[-2:]

        #Setup parameters
        two_params = ['01', '02', '05', '06', '07', '08']
        three_params = ['01', '02', '07', '08']
        if opcode in two_params:
            if param[2] == '0':
                param_1 = intcode[intcode[i+1]]
            else:
                param_1 = intcode[i+1]

            if param[1] == '0':
                param_2 = intcode[intcode[i+2]]
            else:
                param_2 = intcode[i+2]

            if opcode in three_params:
                if param[0] == '0':
                    param_3 = intcode[i+3]
                else:
                    param_3 = intcode[i+3]

        if opcode == '01':
            intcode[param_3] = param_1 + param_2
            i += 4
        elif opcode == '02':
            intcode[param_3] = param_1 * param_2
            i += 4
        elif opcode == '03':
            intcode[intcode[i+1]] = input_id
            i += 2
        elif opcode == '04':
            if param[2] == '0':
                print(intcode[intcode[i+1]])
            else:
                print(intcode[i+1])
            i += 2
        elif opcode == '05':
            if param_1 != 0:
                i = param_2
            else:
                i += 3
        elif opcode == '06':
            if param_1 == 0:
                i = param_2
            else:
                i += 3
        elif opcode == '07':
            if param_1 < param_2:
                intcode[param_3] = 1
            else:
                intcode[param_3] = 0
            i += 4
        elif opcode == '08':
            if param_1 == param_2:
                intcode[param_3] = 1
            else:
                intcode[param_3] = 0
            i += 4

if __name__ == "__main__":
    main()