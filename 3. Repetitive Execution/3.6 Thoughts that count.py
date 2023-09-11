red_white = int(input())
blue_white = int(input())
operator_r_w = input()

for i in range(1, red_white + 1):
    white = i
    red = red_white - white
    blue = blue_white - white

    if blue > 1 and white > 1 and red > 1:
        if operator_r_w == '<':
            if red < white:
                print(blue, white, red)
        else:
            if red > white:
                print(blue, white, red)
