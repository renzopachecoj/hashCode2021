inDir = "in/"
outDir = "out/"
files = ['a','b','c','d','e','f']

for fileName in files:
    f = open(inDir+fileName+".txt", "r")

    D = 0 #duration
    I = 0 #n intersections
    S = 0 #streets
    V = 0 #cars
    F = 0 #bonus points
    streets = {}
    cars = []

    #PARSING INPUT DATA
    count = 0
    line = f.readline()
    while(line):
        data = line.strip().split(" ")
        if count==0:
            D = int(data[0])
            I = int(data[1])
            S = int(data[2])
            V = int(data[3])
            F = int(data[4])
        elif count<=S:
            streets[data[2]] = [int(data[0]), int(data[1]), int(data[3])]
        else:
            data[0] = int(data[0])
            cars.append([data[0],data[1:]])
        count+=1
        line = f.readline()

    '''
    print(D, I, S, V, F)
    for street in streets:
        print(street, '->', streets[street])
    for car in cars:
        print(car)
    '''

    streetDemand = {}
    for car in cars:
        for streetName in car[1]:
            if (not streetName in streetDemand.keys()):
                streetDemand[streetName] = 1
            else:
                streetDemand[streetName] += 1
    
    maxDemand = max(streetDemand.values())
    mostDemanded = {}
    if(S>50000):
        for street in streetDemand:
            if (streetDemand[street] >= maxDemand*0.10):
                mostDemanded[street] = streets[street]
    else:
        mostDemanded = streets
    
    intersections = {}
    for street in streets:
        inter = streets[street][1]
        if (not inter in intersections.keys()):
            intersections[inter] = []
            intersections[inter].append(street)
        else:
            intersections[inter].append(street)

    scheduledInter = {}
    scheduledStreets = set()
    for street in mostDemanded:
        inter = mostDemanded[street][0]
        for incoming in intersections[inter]:
            if (not incoming in scheduledStreets):
                if (not inter in scheduledInter.keys()):
                    scheduledInter[inter] = []
                    scheduledInter[inter].append([incoming, streets[street][2]])
                    scheduledStreets.add(incoming)
                else:
                    scheduledInter[inter].append([incoming, streets[street][2]])
                    scheduledStreets.add(incoming)

    sub_file = open(outDir+fileName+"_submission.txt", "w")
    sub_file.write(str(len(scheduledInter)))
    for intersection in scheduledInter:
        sub_file.write("\n"+str(intersection))
        sub_file.write("\n"+str(len(scheduledInter[intersection])))
        for street in scheduledInter[intersection]:
            sub_file.write("\n"+str(street[0])+" "+str(street[1]))
    sub_file.close()
    print("***DONE***")
