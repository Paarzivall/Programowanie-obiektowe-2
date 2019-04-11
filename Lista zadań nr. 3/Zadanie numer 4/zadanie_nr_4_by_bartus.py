def gen_time(start, stop, hop):
    lStart = list(start)

    while True:
        yield tuple(lStart)
        tmpH = lStart[0] + hop[0]
        tmpMin = lStart[1] + hop[1]
        tmpSec = lStart[2] + hop[2]

        if tmpH > stop[0]:
            break
        else:
            if tmpH >= 24:
                lStart[0] = 0
            else:
                lStart[0] += hop[0]

            if tmpMin > stop[1] and lStart[0] >= stop[0]:
                break
            else:
                if tmpMin >= 60:
                    lStart[0] += 1
                    lStart[1] = tmpMin - 60
                else:
                    lStart[1] += hop[1]

                if tmpSec > stop[2] and lStart[1] >= stop[1] and lStart[0] >= stop[0]:
                    break
                else:
                    if tmpSec >= 60:
                        lStart[1] += 1
                        lStart[2] = tmpSec - 60
                    else:
                        lStart[2] += hop[2]


if __name__ == '__main__':
    for time in gen_time((8, 10, 00), (10, 50, 15), (0, 15, 12)):
        print(time)