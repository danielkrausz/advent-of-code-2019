def main():
    left_boundary = 264360
    right_boundary = 746325

    password_count = 0
    password_count_part2 = 0

    for password in range(left_boundary, right_boundary + 1):
        if is_valid(password):
            password_count += 1
        if is_valid_part2(password):
            password_count_part2 += 1
    
    print(password_count)
    print(password_count_part2)


def is_valid(password):
    has_double = False
    idx = 0
    while idx < len(str(password)) - 1:
        if str(password)[idx] > str(password)[idx + 1]:
            return False
        if str(password)[idx] == str(password)[idx + 1]:
            has_double = True
        idx += 1

    if has_double:
        return True

    return False

def is_valid_part2(password):
    has_double = False
    idx = 0
    while idx < len(str(password)) - 1:
        if str(password)[idx] > str(password)[idx + 1]:
            return False
        if str(password)[idx] == str(password)[idx + 1]:
            j = idx + 1
            repeat_cnt = 0
            while  j < len(str(password)) - 1:
                if str(password)[idx] == str(password)[j+1]:
                    repeat_cnt += 1
                    j += 1
                else:
                    break
            idx += repeat_cnt
            if repeat_cnt == 0:
                has_double = True
        idx += 1

    if has_double:
        return True

    return False

if __name__ == "__main__":
    main()