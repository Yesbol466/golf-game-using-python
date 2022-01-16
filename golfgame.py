names = ["Hole in one!" , "Eagle","Birdie","pari","Bogey", "Double Bogey","Go home!"]
pars  = int(input("How many pars? : "))
strokes = int(input("How many strokes? : "))
if strokes ==1 :
    print(names[0])
elif strokes <= pars - 2:
    print(names[1])
elif strokes == pars - 1:
    print(names[2])
elif strokes == pars:
    print(names[3])
elif strokes == pars + 1:
    print(names[4])
elif strokes == pars + 2:
    print(names[5])
elif strokes >= pars + 3:
    print(names[6])

