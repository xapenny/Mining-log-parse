import sys

def timecalc(start,end):
    starth = int(start[0:2])
    startm = int(start[3:5])
    starts = int(start[6:-1])
    endh = int(end[0:2])
    endm = int(end[3:5])
    ends = int(end[6:-1])
    delta = (endh*3600 + endm*60 + ends) - (starth*3600 + startm*60 + starts)
    return delta

USER = len(sys.argv) - 1
hashsum = 0.0
hashlist = []
timelist = []
xmrlist = []
division = []

for j in range(1,USER+1):
    log = open(str(sys.argv[j]))
    log_line = log.readlines()
    total_hash = 0.0
    total_time = 0
    scale = 3.518275062E-12
    for i in range(1, len(log_line)):
        timeS = log_line[i-1].split()[1][:-5]
        timeE = log_line[i].split()[1][:-5]
        timeDelta = timecalc(timeS,timeE)
        if timeDelta<0:
            timeDelta = 86400 - timeDelta
        spd = log_line[i].split()[5]
        #print("Time Period: {}\tSpeed:{}\t".format(timeDelta, spd))
        total_hash += float(spd)*60
        total_time += timeDelta
        print("{}\t{}\tStart:{}\tEnd:{}".format(total_time,timeDelta,timeS,timeE))
    total_XMR = scale*total_hash
    hashlist.append(str(total_hash))
    hashsum += total_hash
    xmrlist.append(str(total_XMR))
    timelist.append(str(total_time))
    #print("\n\nTotal Hash: {}\nTotal Time: {}s\nTotal XMR: {}".format(total_hash, total_time, total_XMR))
    log.close()

print("\n")
print("{:*^30}".format('Result'))
for i in range(0,USER):
    perc = (float(hashlist[i]) / hashsum) * 100
    print("User {}: \nTotal Hash: {}\nTotal Time: {}s\tabout {:.2f} hours\nTotal XMR: {}\nProportion: {:.2f}%\n".format(sys.argv[i+1], hashlist[i], timelist[i], int(timelist[i])/3600, xmrlist[i], perc))
