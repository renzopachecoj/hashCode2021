from queue import PriorityQueue

inDir = "in/"
outDir = "out/"
files = ['a','b','c','d','e']
for fileName in files:
    f = open(inDir+fileName+".txt", "r")
    line = f.readline()
    count = 0
    pizzas = []
    teams = {
        2: 0,
        3: 0,
        4: 0
    }
    while (line):
        if count==0:
            teamNumbers = line.strip().split(" ")
            for i in range(0,int(teamNumbers[1])):
                teams[2]+=1
            for i in range(0,int(teamNumbers[2])):
                teams[3]+=1
            for i in range(0,int(teamNumbers[3])):
                teams[4]+=1
        else:
            pizzaNumbers = line.strip().split(" ")
            pizzas.append((count-1, pizzaNumbers[1:]))
        line = f.readline()
        count+=1

    deliveries = []
    numIngredientsPQ = PriorityQueue()
    originalityScorePQ = PriorityQueue()
    ingredients = set()

    for pizza in pizzas:
        numIngredientsPQ.put((len(pizza[1]), pizza))

    while(not numIngredientsPQ.empty()):
        pizza = numIngredientsPQ.get()[1]
        originals = 0
        for ingredient in pizza[1]:
            if ingredient in ingredients:
                originals-=1
            else:
                ingredients.add(ingredient)
                originals+=1
        originalityScore = originals+len(pizza[1])
        originalityScorePQ.put((originalityScore, pizza))

    while(not originalityScorePQ.empty()):
        if(originalityScorePQ.qsize()//2>0 and teams[2]>0):
            count = 0
            pizzasForTeam = []
            while(count<2):
                pizzasForTeam.append(originalityScorePQ.get()[1])
                count+=1
            deliveries.append((2,pizzasForTeam))
            teams[2]-=1
        elif(originalityScorePQ.qsize()//3>0 and teams[3]>0):
            count = 0
            pizzasForTeam = []
            while(count<3):
                pizzasForTeam.append(originalityScorePQ.get()[1])
                count+=1
            deliveries.append((3,pizzasForTeam))
            teams[3]-=1
        elif(originalityScorePQ.qsize()//4>0 and teams[4]>0):
            count = 0
            pizzasForTeam = []
            while(count<4):
                pizzasForTeam.append(originalityScorePQ.get()[1])
                count+=1
            deliveries.append((4,pizzasForTeam))
            teams[4]-=1
        else:
            originalityScorePQ.get()

    sub_file = open(outDir+fileName+"_submission.txt", "w")
    sub_file.write(str(len(deliveries)))
    for delivery in deliveries:
        sub_file.write("\n")
        sub_file.write(str(delivery[0]))
        for pizza in delivery[1]:
            sub_file.write(" "+str(pizza[0]))
    sub_file.close()
    print("***DONE***")
