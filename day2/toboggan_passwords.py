def convert_line(line):
    segments = line.rstrip().split(' ')
    range = segments[0].split('-')
    lower = int(range[0])
    upper = int(range[1])
    letter = segments[1][0]
    password = segments[2]
    return lower, upper, letter, password


def valid_password(password):
    if password[0] <= password[3].count(password[2]) and password[1] >= password[3].count(password[2]):
        #print(f"{password[3]} is valid")
        return 1
    return 0


def new_rules(lower, upper, letter, password):
    if (letter == password[lower - 1]) != (letter == password[upper - 1]):
        return 1
    return 0


total_first = 0
total_second = 0

with open('input.txt', 'r') as infile:
    for line in infile:
        converted = convert_line(line)
        total_first += valid_password(converted)
        total_second += new_rules(converted[0],
                                  converted[1],
                                  converted[2],
                                  converted[3])

    print(total_first)
    print(total_second)
