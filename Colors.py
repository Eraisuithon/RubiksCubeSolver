import cv2

ROWS, COLS, FACES = 3, 3, 6


def get_colors():
    def get_cube_colors(image_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not load image from {image_path}")
            return

        image = cv2.resize(image, (300, 300))
        height, width, _ = image.shape

        cell_width = width // COLS
        cell_height = height // ROWS

        cube_colors = []
        for row in range(ROWS):
            row_colors = []
            for col in range(COLS):
                center_x = (col * cell_width) + (cell_width // 2)
                center_y = (row * cell_height) + (cell_height // 2)

                color_bgr = image[center_y, center_x]
                color_rgb = color_bgr[::-1]

                row_colors.append(color_rgb)
            cube_colors.append(row_colors)

        return cube_colors


    image_paths = ['Up.jpg', 'Front.jpg', 'Down.jpg', 'Left.jpg', 'Right.jpg', 'Back.jpg']

    colors = {}
    for image_path in image_paths:
        face_color = get_cube_colors(image_path)
        face = image_path[0]
        colors[face] = {}
        for i in range(ROWS):
            for j in range(COLS):
                colors[face][(i, j)] = face_color[i][j]

    return colors

