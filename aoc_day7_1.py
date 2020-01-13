import Intcode

def generateAmplifierInputs(minimum,maximum):

    #this function generates a 1x5 list of the numbers in between min and max.
    #the numbers will not repeat in the final list.

    avalues = list(range(minimum,maximum+1))
    ampinputs = []

    for a in avalues:
        bvalues = avalues.copy()
        bvalues.remove(a)
        for b in bvalues:
            cvalues = bvalues.copy()
            cvalues.remove(b)
            for c in cvalues:
                dvalues = cvalues.copy()
                dvalues.remove(c)
                for d in dvalues:
                    evalues = dvalues.copy()
                    evalues.remove(d)
                    for e in evalues:
                        ampinputs.append([a,b,c,d,e])

    return ampinputs

def runAmplifier(cmdinput,ampinputs,startValue):

    #this function creates the amplifiers, and runs a once pass through to get
    #the output of amplifier E.

    ampList = []
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier A"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier B"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier C"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier D"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier E"))

    ampList[0].setInputs([ampinputs[0],startValue])
    ampList[0].run()
    ampList[1].setInputs([ampinputs[1],ampList[0].outputs[-1]])
    ampList[1].run()
    ampList[2].setInputs([ampinputs[2],ampList[1].outputs[-1]])
    ampList[2].run()
    ampList[3].setInputs([ampinputs[3],ampList[2].outputs[-1]])
    ampList[3].run()
    ampList[4].setInputs([ampinputs[4],ampList[3].outputs[-1]])
    end = ampList[4].run()

    return ampList[4].outputs[-1]

def getFeedback(cmdinput,ampList,startValue):

    #this function simply sets each amplifiers output to the input of the next
    #amplifier, and returns a value.

    ampList[0].setInputs([startValue])
    ampList[0].run()
    ampList[1].setInputs([ampList[0].outputs[-1]])
    ampList[1].run()
    ampList[2].setInputs([ampList[1].outputs[-1]])
    ampList[2].run()
    ampList[3].setInputs([ampList[2].outputs[-1]])
    ampList[3].run()
    ampList[4].setInputs([ampList[3].outputs[-1]])
    end = ampList[4].run()

    return ampList, end

def runFeedbackLoop(cmdinput,ampinputs,startValue):

    #create the amplifiers.
    ampList = []
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier A"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier B"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier C"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier D"))
    ampList.append(Intcode.Intcode(cmdinput,name="Amplifier E"))

    #start the amplifiers with the ampinputs. The first input of the Intcode
    #is the ampinput.
    for i,j in enumerate(ampList):
        j.setInputs([ampinputs[i]])
        j.run()

    i = 0
    end = 0

    #This is the feedback loop. getFeedback will apply each amplifiers outputs
    #to the next amplifier, A->B->C->D->E->A. When getFeedback returns '99'
    #(opcode for the program finishing), then the feedback loop is done.
    #return the startValue which at the end will be the output of Amplifier E.
    while end != 99:

        ampList,end = getFeedback(cmdinput,ampList,startValue)
        startValue = ampList[-1].outputs[-1]

        #failsafe for infitite loop
        i += 1
        if i > 100:
            break

    return startValue

def part1(cmdinput):

    ampinputs = generateAmplifierInputs(0,4)

    startValue = 0
    ampEoutput = 0
    ampEmax = 0

    #this loop runs the main function of part one, runAmplifier, for each
    #amplifier input and returns the maximum.
    for i in ampinputs:
        ampEoutput = runAmplifier(cmdinput,i,startValue)
        if ampEoutput > ampEmax:
            ampEmax = ampEoutput

    #part 1 answer (11828):
    print('part 1 answer:',ampEmax)

def part2(cmdinput):

    ampinputs = generateAmplifierInputs(5,9)

    startValue = 0
    ampEoutput = 0
    ampEmax = 0

    #this loop runs the main function of part two, runFeedbackLoop, for each
    #amplifier input and returns the maximum.
    for i in ampinputs:
        ampEoutput = runFeedbackLoop(cmdinput,i,startValue)
        if ampEoutput > ampEmax:
            ampEmax = ampEoutput

    #part 2 answer (11828):
    print('part 2 answer:',ampEmax)


if __name__ =="__main__":

    #read the numbers in
    #readfile = open('aoc_day7_test.txt')
    readfile = open('aoc_day7_1.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    cmdinput = list(map(int,fileinput[0].split(',')))

    #part 1 solution
    part1(cmdinput)

    #part 2
    part2(cmdinput)





#comment
