import numpy as np

# Definiowanie macierzy
front = np.full((3,3), 1)
left = np.full((3,3), 2)
right = np.full((3, 3), 3)
up = np.full((3, 3), 4)
bottom = np.full((3, 3), 5)
back = np.full((3, 3), 6)

print(front)
print(up)

def rotate_front(front, left, right, up, bottom, direction):
    if direction == 90:
        # Obracanie macierzy front o 90 stopni w prawo
        front[:] = np.rot90(front, 1)
        
        # Aktualizacja macierzy sąsiadujących zgodnie z ruchem kostki Rubika
        # Przechowujemy zmieniane wiersze i kolumny
        last_row_up = up[-1, :].copy()
        first_col_right = right[:, 0].copy()
        first_row_bottom = bottom[0, :].copy()
        last_col_left = left[:, -1].copy()
        
        up[-1, :] = np.flip(last_col_left)
        right[:, 0] = last_row_up
        bottom[0, :] = np.flip(first_col_right)
        left[:, -1] = first_row_bottom
        
    elif direction == -90:
        # Obracanie macierzy front o 90 stopni w lewo
        front[:] = np.rot90(front, -1)
        
        # Aktualizacja macierzy sąsiadujących zgodnie z ruchem kostki Rubika
        # Przechowujemy zmieniane wiersze i kolumny
        last_row_up = up[-1, :].copy()
        first_col_right = right[:, 0].copy()
        first_row_bottom = bottom[0, :].copy()
        last_col_left = left[:, -1].copy()
        
        up[-1, :] = first_col_right
        right[:, 0] = np.flip(first_row_bottom)
        bottom[0, :] = last_col_left
        left[:, -1] = np.flip(last_row_up)
    
    else:
        raise ValueError("Direction must be either 90 or -90")


# Wywołanie funkcji dla obrotu o 90 stopni w prawo
print("Before 90 degrees right:")
print("Front:\n", front)
print("Left:\n", left)
print("Right:\n", right)
print("Up:\n", up)
print("Bottom:\n", bottom)

rotate_front(front, left, right, up, bottom, 90)

print("\nAfter 90 degrees right:")
print("Front:\n", front)
print("Left:\n", left)
print("Right:\n", right)
print("Up:\n", up)
print("Bottom:\n", bottom)

# Wywołanie funkcji dla obrotu o 90 stopni w lewo, aby przywrócić stan
rotate_front(front, left, right, up, bottom, -90)

print("\nAfter 90 degrees left:")
print("Front:\n", front)
print("Left:\n", left)
print("Right:\n", right)
print("Up:\n", up)
print("Bottom:\n", bottom)