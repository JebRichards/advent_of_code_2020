def readEntries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [int(line.rstrip()) for line in filein]


def sum_of_2020(entries):
    entries_set = set(entries)
    for i in entries_set:
        if (2020 - i) in entries_set:
            return i * (2020 - i)


def three_2020(entries):
    entries_set = set(entries)
    for i in entries_set:
        for j in entries:
            if (2020 - (i + j)) in entries_set:
                return i * j * (2020 - (i + j))


def main():
    entries = readEntries()
    print(sum_of_2020(entries))
    print(three_2020(entries))


main()
