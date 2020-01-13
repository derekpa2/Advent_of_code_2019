import Intcode
import sys

def runtestcases():

    if testcase == 1:
        cmdinput = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    elif testcase == 2:
        cmdinput = [1102,34915192,34915192,7,4,7,99,0]
    elif testcase == 3:
        cmdinput = [104,1125899906842624,99]

    test = Intcode.Intcode(cmdinput,debug=True)

    test.run()

    if testcase == 1:
        print(test.outputs)
        if cmdinput == test.outputs:
            print('PASSES!')
        else:
            print('FAILS!')

    if testcase == 2:
        print(test.outputs[-1])
        if len(str(test.outputs[-1])) == 16:
            print('PASSES!')
        else:
            print('FAILS!')

    if testcase == 3:
        print(test.outputs[-1])
        if test.outputs[-1] == 1125899906842624:
            print('PASSES!')
        else:
            print('FAILS!')


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
    readfile = open('aoc_day9.txt')

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
