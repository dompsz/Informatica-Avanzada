def draw_triangle(x):
    if x <= 0:
        print("input error")
        return

    for i in range(1, x + 1):
        print("* " * i)

draw_triangle(int(input("pick size: ")))