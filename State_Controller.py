faces = ['U', 'F', 'D', 'L', 'R', 'B']


def state(colors):
    final = ''
    for face in faces:
        for i in range(3):
            for j in range(3):
                final += colors[face][(i, j)]
    return final


def show(color_groups):
    for key, value in color_groups.items():
        for i in range(3):
            for j in range(3):
                print(value.get((i, j), None), end='  ')
            print()
        print('---')


def show_state(s):
    for f in range(6):
        for i in range(3):
            for j in range(3):
                print(s[f * 9 + i * 3 + j], end=' ')
            print()
        print('---')


