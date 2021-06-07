def trees_hit(trees, x, y):
    current_x = 0
    current_y = 0
    total_trees = 0
    while current_y < len(trees):
        if trees[current_y][current_x % len(trees[0])] == '#':
            total_trees += 1
        current_x += x
        current_y += y
    return total_trees


def five_slopes(trees):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multi_trees = 1
    for i in slopes:
        multi_trees *= trees_hit(trees, i[0], i[1])
    return multi_trees


def main():
    with open("input.txt", "r") as infile:
        tree_arr = list(map(lambda x: x.rstrip(), infile.readlines()))
        print(trees_hit(tree_arr, 3, 1))
        print(five_slopes(tree_arr))


main()
