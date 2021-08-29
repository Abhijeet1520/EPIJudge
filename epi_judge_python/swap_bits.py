from test_framework import generic_test


def swap_bits(x, i, j):
    if bool(x & 1<<i) ^ bool(x & 1<<j):
        x ^= 1<<j ^ 1<<i
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
