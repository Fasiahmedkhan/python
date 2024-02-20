


def calculate_area(length, width):
    area = (length * width)
    return area


length = float(input("length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)
print("The area of the rectangle is:", area)
