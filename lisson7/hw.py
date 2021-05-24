plane = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"],
]


def check_winner(p):
    win = True
    for i in range(3):
        row = plane[i]
        start = ""
        for k in row:
            if k == "*":
                win = False
                break
            if not start:
                start = k
            else:
                win = False
                if start == k:
                    start = k
                else:
                    break


        if win:
            return start




def input_x_y():
    return int(input()) - 1, int(input()) - 1


def print_plane(plane):
    for i in range(3):
        row = plane[i]
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i != 2:
            print("-"*9)

print(check_winner(plane))






