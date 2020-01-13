import Intcode

if __name__ =="__main__":

    #read the numbers in
    readfile = open('aoc_day5_1.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    cmdinput = list(map(int,fileinput[0].split(',')))

    Intcode.Intcode(cmdinput,[5]).run()

#comment
