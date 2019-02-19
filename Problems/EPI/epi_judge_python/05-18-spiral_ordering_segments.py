from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    n = len(square_matrix)
    spiral_order = []

    for _ in range(n ** 2):
        spiral_order.append(square_matrix[x][y])
        square_matrix[x][y] = None
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]

        if (next_x not in range(n)
                or next_y not in range(n)
                or square_matrix[next_x][next_y] is None):
            direction = (direction + 1) % 4
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]

        x, y = next_x, next_y
    return spiral_order


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-18-spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
