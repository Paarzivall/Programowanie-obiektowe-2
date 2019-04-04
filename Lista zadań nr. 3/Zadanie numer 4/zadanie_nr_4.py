def gen_time(start, stop, hop):
    czasStart = list(start)
    czasStop = list(stop)
    czasHop = list(hop)
    print(type(czasStart))
    """while czasStart[0]<=czasStop[0]and czasStart[1]<=czasStop[1]and czasStart[2]<=czasStop[2]:
        tmp = czasStart[1]+czasHop[1]
        tmp2 = czasStart[2]+czasHop[2]
        if tmp>=60:
            czasStart[1]+=tmp-60
            czasStart[0]+=1
        if tmp2>=60:
            tmp2-=60
            czasStart[2]+=tmp2
            czasStart[1]+=1

        yield czasStart"""



if __name__ == '__main__':

    for time in gen_time((8,10,0),(10,50,15),(0,15,12)):
        print(time)
