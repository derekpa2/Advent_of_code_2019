import Intcode

class IntcodeTest:

    def __init__(self,testname,testcase,solution):
        self.testname = testname
        self.testID,self.testtype,self.iteration = self.returnTestParams(testname)
        self.testcase = testcase
        self.solution = solution
        self.succcess = False

    def returnTestParams(self,testname):

        testID = testname[4:]
        testsplit = testname.split('.')
        testtype = int(testsplit[0][4:])
        iteration = int(testsplit[1])

        return testID,testtype,iteration

def printTestOutcome(intcodeObject,intcodeTestObject,failedID,testpass):

    #testObject needs to be of type Intcode

    print('\n')

    if intcodeObject.commandline == intcodeTestObject.solution:
        print(intcodeTestObject.testname + ' Passes!')
        testpass += 1
    else:
        print('Test fails...')
        failedID.append(intcodeTestObject)

    print('\n')

    return testpass

def printTotalTestsOutcome(failedID,testpass,totaltests):

    print('Total tests passed: ' + str(testpass) + '/' + str(totaltests) + '\n')

    print('Tests Failed:')
    if len(failedID) > 0:
        for i in failedID:
            print(i.testname)
    else:
        print('No tests failed!')
    print('\n')

if __name__ =="__main__":

    #read the numbers in
    #readfile = open('aoc_day7_test.txt')
    readfile = open('Intcode_test.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line.strip())

    #creates a test dictionary. The key is the test name, value is a 2-D list
    #where the command input and solution are the 1st and 2nd lists
    #respectively.

    testCases = []
    i = 0

    while i < len(fileinput):
        if fileinput[i][0:4] == 'TEST':
            testinput = list(map(int,fileinput[i+1].split(',')))
            testoutput = list(map(int,fileinput[i+2].split(',')))
            testCases.append(IntcodeTest(fileinput[i],testinput,testoutput))
            i += 3
        i += 1

    testpass = 0
    failedID = []

    for j in testCases:

        tempIntcode = Intcode.Intcode(j.testcase,debug=True)
        tempIntcode.run()
        testpass = printTestOutcome(tempIntcode,j,failedID,testpass)


    printTotalTestsOutcome(failedID,testpass,3)
    #numtests = len(cmdinput)/2

    #print(cmdinput[0])

    #test1 = Intcode.Intcode(cmdinput[0],name='Test #1',debug=True)
    #test1.run()

    #testpass = printTestOutcome(test1,testpass,1)







#end
