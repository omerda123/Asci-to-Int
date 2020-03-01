NUMS = {
    0: 63,
    1: 48,
    2: 109,
    3: 121,
    4: 114,
    5: 91,
    6: 95,
    7: 49,
    8: 127,
    9: 123
}


def solve_one_line(array: list):
    print(array)
    res = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, line in enumerate(array):
        for j, c in enumerate(line):
            if i == 0 and ord(c) == 95:
                res[int(j / 3)] += 1
            elif i == 1:
                if ord(c) == 95:
                    res[int(j / 3)] += 64
                elif ord(c) == 124 and j % 3 == 0:
                    res[int(j / 3)] += 2
                elif ord(c) == 124:
                    res[int(j / 3)] += 32
            elif i == 2:
                if ord(c) == 95:
                    res[int(j / 3)] += 8
                elif ord(c) == 124 and j % 3 == 0:
                    res[int(j / 3)] += 4
                elif ord(c) == 124:
                    res[int(j / 3)] += 16
    return res;


arr = []
res = []
with open("simple_input.txt") as f:
    for i, line in enumerate(f):
        arr.append(line)
        if i % 2 == 0 and i != 0:
            solve_one_line(arr[i-2:i+1])
# print(res)
