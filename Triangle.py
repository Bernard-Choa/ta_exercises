def triangle_drawer():
    h = int(input("Input height of triangle: "))
    for i in range(h, 0, -1):
        if i == 1:
            print((" " * i) + "/" + ("_" * (h-i)) + "|")
        else:
            print((" " * i) + "/" + (" " * (h-i)) + "|")


triangle_drawer()