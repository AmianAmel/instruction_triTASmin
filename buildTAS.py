import random
x=random.sample(range(-10,100), random.randrange(5,15))

for i in range(0, len(x)):
    tas_min=insert_value(x[i]) # type: ignore
     showtasmin(tas_min) # type: ignore
def insert_value(x):
    tas_min.append(x)
    j = len(tas_min)
    while( (tas_min[j-1] < tas_min[int(j/2)-1]) and j-1 > 0):

        temp = tas_min[j-1]
        tas_min[j-1] = tas_min[int(j/2)-1]
        tas_min[int(j/2)-1] = temp
        j = int(j/2)
    return tas_min
def showtasmin(x):
    tas_min=[]
    binary = 0
    j = pow(2, binary)
    offset = 0
    temp = []

    for i in range(0, len(x)):

        if (i < j + offset):
            temp.append(x[i])
        else:
            tas_min.append(temp)
            temp = []
            binary += 1
            j = pow(2, binary)
            offset = i
            temp.append(x[i])

    tas_min.append(temp)

    print("\n final result:\n", tas_min)