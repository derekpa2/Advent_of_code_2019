import Intcode
import sys

def runtestcases():

    if testcase == 1:
        continue
    elif testcase == 2:
        continue
    elif testcase == 3:
        continue

    test = Intcode.Intcode(cmdinput,debug=True)

    test.run()

    if testcase == 1:
        continue
    if testcase == 2:
        continue
    if testcase == 3:
        continue

def part1(cmdinput):

    boost = Intcode.Intcode(cmdinput,debug=True)

    boost.setInputs(1)

    boost.run()

def part2(cmdinput):

    boost = Intcode.Intcode(cmdinput,debug=True)

    boost.setInputs(2)

    boost.run()


if __name__ =="__main__":

    #read the numbers in
    #readfile = open('aoc_day7_test.txt')
    readfile = open('aoc_day11.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    cmdinput = list(map(int,fileinput[0].split(',')))

    testcase = int(sys.argv[1])

    if testcase > 0 and testcase < 4:
        runtestcases()

    #part 1 solution
    if sys.argv[2] == 'day1':
        part1(cmdinput)

    #part 2
    if sys.argv[2] == 'day2':
        part2(cmdinput)
