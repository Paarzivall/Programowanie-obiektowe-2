def gen_time(start, stop, hop):
    czasStart = list(start)
    czasStop = list(stop)
    czasHop = list(hop)

    while True:
        tupla = (czasStart[0], czasStart[1], czasStart[2])
        yield tupla
        tmp_h = czasStart[0] + czasHop[0]
        tmp_min = czasStart[1] + czasHop[1]
        tmp_sec = czasStart[2] + czasHop[2]
        if tmp_h >= 24:
            czasStart[0] = 0
        else:
            czasStart[0] += czasHop[0]

        if tmp_sec >= 60:
            czasStart[1] += 1
            czasStart[2] = tmp_sec - 60
        else:
            czasStart[2] += czasHop[2]

        if tmp_min >= 60:
            czasStart[0] += 1
            czasStart[1] = tmp_min - 60
        else:
            czasStart[1] += czasHop[1]

        if czasStart[0] >= czasStop[0]:
            if czasStart[1] >= czasStop[1]:
                break


if __name__ == '__main__':

    for time in gen_time((8, 10, 0), (10, 50, 15), (0, 15, 12)):
        print(time)
