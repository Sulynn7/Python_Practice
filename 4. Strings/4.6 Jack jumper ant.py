ant_line1 = input()
ant_line2 = input()

ants = list(ant_line1[::-1] + ant_line2)

c = 0

while 1:
    print(''.join(ants))

    if ''.join(ants) == ant_line2 + ant_line1[::-1]:
        break

    converted_ant = []

    for i, ant in enumerate(tuple(ants)):
        try:
            if (ant in ant_line1) and (ants[i + 1] in ant_line2):
                if (ant not in converted_ant) and (ants[i + 1] not in converted_ant):
                    converted_ant.append(ant)
                    converted_ant.append(ants[i + 1])

                    ants[i] = ants[i + 1]
                    ants[i + 1] = ant

        except IndexError:
            pass