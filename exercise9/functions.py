from math import pi


def show_personal_info():
    print("John Williams")
    print("Rovaniemi")
    print("Software engineer")


def count_seconds():
    txt = input("Give time in format 'Xh Xmin Xsec'")
    txt_processed = txt.split(" ")  # Splitting input to list
    hours = txt_processed[0][:-1]  # Extracting only numbers from list elements
    minutes = txt_processed[1][:-3]
    seconds = txt_processed[2][:-3]
    result = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
    return result


def magazine_serial_check(serial):
    check = False
    if len(serial) == 9:  # Firstly we check for correct length
        if serial[0:3].isdigit() and serial[-4:-1].isdigit():  # Then if every symbol except middle one is number
            if serial[4] == "-":  # Finally checking middle symbol
                check = True  # If any of conditions unmatched check variable stay False
    return check


def show_numbered_list(title, data):
    print(f"{title}:")
    for el in data:
        print(f"{int(data.index(el)) + 1}. {el}")  # Printing out order number and name


def box_volume(width, height, depth):
    result = width * height * depth
    return round(result, 2)


def ball_volume(radius):
    result = (4 * pi * (radius ** 3)) / 3
    return round(result, 2)


def pipe_volume(radius, length):
    result = pi * (radius ** 2) * length
    return round(result, 2)

