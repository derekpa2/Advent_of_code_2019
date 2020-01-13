
def Intcode(cmdinput,noun,verb):

    #begin Intcode function.
    #
    #This function takes a cmdinput string, replaces index 1 with noun,
    #replaces index 2 with verb, and returns the output at 0
    #
    #
    cmdinput[1] = noun
    cmdinput[2] = verb

    index = 0

    while index < len(cmdinput):

        if cmdinput[index] == 1:
            cmdinput[cmdinput[index + 3]] = cmdinput[cmdinput[index + 1]] + cmdinput[cmdinput[index + 2]]
            index = index + 4
        elif cmdinput[index] == 2:
            cmdinput[cmdinput[index + 3]] = cmdinput[cmdinput[index + 1]] * cmdinput[cmdinput[index + 2]]
            index = index + 4
        elif cmdinput[index] == 99:
            index = len(cmdinput)
        else:
            index = index + 1

    return cmdinput

if __name__ =="__main__":

    #read the numbers in
    readfile = open('aoc_day2_1.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    #splits the string up and makes it into a list of integers
    #map(x,y) assigns the list y to a type x, and returns a list object
    #list(map(x,y)) converts that list object to a list
    cmdinput = list(map(int,fileinput[0].split(',')))

    #This is the result of passing the cmdinput string, the noun of 12,
    #and the verb of 2 to the Intcode function.
    result = Intcode(cmdinput,12,2)

    print(result)
