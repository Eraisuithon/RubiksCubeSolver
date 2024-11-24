from Colors import get_colors

def get_color_groups():
    faces = ['U', 'F', 'D', 'L', 'R', 'B']
    colors = get_colors()
    color_groups = {}
    for face in faces:
        color_groups[face] = {(1, 1): face}

    for face in faces:
        for i in range(3):
            for j in range(3):
                min_dist = 3 * 255**2
                min_face = None
                color = colors[face][(i, j)]
                for center_face in faces:
                    center = colors[center_face][(1, 1)]
                    dist = sum(((int(c1)-int(c2))**2 for c1, c2 in zip(color, center)))
                    if dist <= min_dist:
                        min_dist = dist
                        min_face = center_face

                color_groups[face][(i, j)] = min_face

    return color_groups

