def main():
    left_boundary = 264360
    right_boundary = 746325

    password_count = 0

    for password in range(left_boundary, right_boundary + 1):
        if is_valid(password):
            password_count += 1
    
    print(password_count)

def is_valid(password):
    has_double = False
    idx = 0
    while idx < len(str(password)) - 1:
        if str(password)[idx] == str(password)[idx + 1]:
            has_double = True
        if str(password)[idx] > str(password)[idx + 1]:
            return False
        idx += 1

    if has_double:
        return True

    return False

if __name__ == "__main__":
    main()